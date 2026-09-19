# Infraestrutura Local — Docker Compose

Este documento explica os containers usados pela Nasty-Plattform, o que é
o Docker Compose e como montar/gerir o ambiente local.

## Índice

1. [O que é o Docker Compose](#o-que-é-o-docker-compose)
2. [Containers](#containers)
3. [Pré-requisitos](#pré-requisitos)
4. [Como montar o ambiente](#como-montar-o-ambiente)
5. [Verificar / testar cada serviço](#verificar--testar-cada-serviço)
6. [Parar, limpar e persistência](#parar-limpar-e-persistência)
7. [Notas e próximos passos](#notas-e-próximos-passos)

---

## O que é o Docker Compose

[Docker Compose](https://docs.docker.com/compose/) é uma ferramenta para
definir e correr **múltiplos containers como um único stack**, descrito
num ficheiro declarativo (`docker-compose.yaml`). Em vez de correres
`docker run` várias vezes com flags diferentes para cada serviço (broker
MQTT, base de dados, etc.), descreves tudo uma vez — imagem, portas,
variáveis de ambiente, volumes, dependências entre serviços — e o Compose
trata de criar a rede interna, subir os containers pela ordem certa e
mantê-los geridos como um grupo.

Vantagens para este projeto:
- **Reprodutibilidade** — qualquer pessoa (ou tu, daqui a 3 meses) sobe a
  infra inteira com um comando, sem instalar Mosquitto/Postgres/ClickHouse
  à mão.
- **Isolamento** — cada serviço corre no seu próprio container, com a sua
  versão fixa, sem conflitos com o que tiveres instalado na máquina.
- **Progressão por fases** — usamos `profiles` (ver abaixo) para subires
  apenas os containers relevantes à fase do roadmap em que estás.

O ficheiro principal está em [`docker-compose.yaml`](./docker-compose.yaml).

---

## Containers

| Serviço | Imagem | Papel na plataforma | Fase | Documentação oficial |
|---|---|---|---|---|
| `mosquitto` | [`eclipse-mosquitto:2`](https://hub.docker.com/_/eclipse-mosquitto) | Broker MQTT — recebe as leituras publicadas pelo ESP32 (ou pelo simulador) e entrega-as ao Ingestion Service | Fase 2–3 | [Mosquitto docs](https://mosquitto.org/documentation/) |
| `postgres` | [`postgres:16-alpine`](https://hub.docker.com/_/postgres) | Armazena o *last value* de cada sensor — o que a Api/Dashboard consulta para o estado atual | Fase 4 | [PostgreSQL docs](https://www.postgresql.org/docs/16/) |
| `clickhouse` | [`clickhouse/clickhouse-server:24-alpine`](https://hub.docker.com/r/clickhouse/clickhouse-server) | Armazena o histórico de séries temporais para os gráficos do dashboard | Fase 7 | [ClickHouse docs](https://clickhouse.com/docs) |
| `prometheus` | [`prom/prometheus`](https://hub.docker.com/r/prom/prometheus) | Recolhe métricas expostas pela Api/Ingestion (latência, throughput, erros) | Fase 9 | [Prometheus docs](https://prometheus.io/docs/introduction/overview/) |
| `grafana` | [`grafana/grafana`](https://hub.docker.com/r/grafana/grafana) | Dashboards de observabilidade sobre as métricas do Prometheus | Fase 9 | [Grafana docs](https://grafana.com/docs/grafana/latest/) |

`Ingestion/`, `Api/` e `Platform/` **não** estão no compose para já — nesta
fase corres cada um localmente (`go run`, `./mvnw quarkus:dev`, `ng serve`)
para teres hot-reload rápido. Podem ser adicionados ao compose mais tarde
(Fase 8/9, quando fizer sentido "dockerizar" tudo para testar em conjunto).

### Ficheiros de configuração

- [`mosquitto/config/mosquitto.conf`](./mosquitto/config/mosquitto.conf) —
  listener MQTT (1883) e MQTT-sobre-WebSocket (9001), sem autenticação
  (`allow_anonymous true`). Adequado só para desenvolvimento local.
- [`prometheus/prometheus.yml`](./prometheus/prometheus.yml) — scrape
  config mínima; expandir quando a Api/Ingestion expuserem um endpoint
  `/metrics`.

---

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e o plugin
  [Docker Compose v2](https://docs.docker.com/compose/install/)
  (`docker compose version` deve funcionar — sem hífen, é o plugin novo).

---

## Como montar o ambiente

Os serviços estão agrupados em **profiles**, um por fase, para não teres
de subir tudo de uma vez:

| Profile | Sobe |
|---|---|
| `mqtt` | `mosquitto` |
| `postgres` | `postgres` |
| `clickhouse` | `clickhouse` |
| `observability` | `prometheus` + `grafana` |
| `full` | todos os serviços acima |

```bash
# a partir da raiz do repo

# Exemplo: só precisas do broker MQTT para testar o simulador + Ingestion
docker compose -f Deployment/Local/docker-compose.yaml --profile mqtt up -d

# Quando chegares à Fase 4, adicionas o Postgres
docker compose -f Deployment/Local/docker-compose.yaml --profile mqtt --profile postgres up -d

# Ou, para subir tudo de uma vez
docker compose -f Deployment/Local/docker-compose.yaml --profile full up -d
```

`-d` corre em background (*detached*). Sem `--profile`, `docker compose up`
não sobe nenhum serviço — é intencional (ver comentário no topo do
`docker-compose.yaml`).

---

## Verificar / testar cada serviço

```bash
# Ver o que está a correr
docker compose -f Deployment/Local/docker-compose.yaml ps

# Logs de um serviço específico
docker compose -f Deployment/Local/docker-compose.yaml logs -f mosquitto

# Testar o Mosquitto (precisa de mosquitto-clients instalado, ou usa um container)
docker run --rm --network host eclipse-mosquitto:2 \
  mosquitto_pub -h localhost -t "sensors/test" -m '{"hello":"world"}'

# Testar o Postgres
docker exec -it nasty-postgres psql -U nasty -d nasty -c "SELECT 1;"

# Testar o ClickHouse
curl "http://localhost:8123/?query=SELECT%201"

# UIs no browser
open http://localhost:9090   # Prometheus
open http://localhost:3000   # Grafana (login inicial: admin/admin)
```

---

## Parar, limpar e persistência

```bash
# Parar os containers (mantém os volumes/dados)
docker compose -f Deployment/Local/docker-compose.yaml --profile full stop

# Parar e remover os containers (mantém os volumes/dados)
docker compose -f Deployment/Local/docker-compose.yaml --profile full down

# Apagar tudo, incluindo os dados persistidos (Postgres, ClickHouse, etc.)
docker compose -f Deployment/Local/docker-compose.yaml --profile full down -v
```

Cada serviço com estado (`postgres`, `clickhouse`, `mosquitto`, `prometheus`,
`grafana`) usa um **named volume** (definido no fim do `docker-compose.yaml`),
por isso os dados sobrevivem a um `down` normal — só desaparecem com `-v`.

---

## Notas e próximos passos

- Este `README.md` é a fonte de verdade sobre a infraestrutura local
  *neste repositório*. Se vierem a usar um vault Obsidian separado para
  arquitetura/roadmap, liguem esse documento aqui em vez de duplicar.
- Quando o simulador de dados (a substituir o ESP32 temporariamente)
  estiver pronto, o mais natural é adicioná-lo também como serviço no
  compose (profile `mqtt`, por exemplo), para subir broker + simulador
  com um único comando.
- Credenciais neste ficheiro (`nasty`/`nasty`, Grafana `admin`/`admin`)
  são só para desenvolvimento local — nunca reutilizar em deploy real.
