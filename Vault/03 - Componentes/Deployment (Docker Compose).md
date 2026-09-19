# Deployment (Docker Compose)

← [[00 - Home|Home]]

Nota de estudo sobre a infraestrutura local do projeto: que containers
existem, porque existem, e como o Docker Compose os organiza. Para os
comandos exatos do dia a dia (subir/parar/testar), ver
`Deployment/Local/README.md` no repo — este ficheiro foca-se no
*porquê*, aquele no *como*.

## Papel na arquitetura

A infra local dá suporte aos componentes descritos em
[[Arquitetura Geral]]: o broker MQTT liga o firmware (ou o simulador —
ver nota sobre substituir o ESP32) ao Ingestion Service; o Postgres e o
ClickHouse são os dois destinos de escrita da Api, conforme o
[[Contrato de Dados]]; o Prometheus/Grafana ficam de fora do caminho
funcional — servem só observabilidade (Fase 9 do [[Roadmap]]).

Nenhum destes containers substitui o trabalho de implementar os
componentes (`Ingestion/`, `Api/`, `Platform/`) — são só a
infraestrutura à volta deles.

## O que é o Docker Compose

Docker Compose é uma ferramenta para descrever **múltiplos containers
como um único stack**, num ficheiro declarativo
(`docker-compose.yaml`), em vez de correr `docker run` à mão para cada
serviço com as suas próprias flags. O ficheiro descreve, por serviço:
imagem, portas expostas, variáveis de ambiente, volumes (para
persistência) e dependências entre serviços. O Compose garante que a
rede interna entre containers é criada automaticamente (cada serviço
consegue resolver os outros pelo nome, ex. `postgres:5432` a partir de
outro container) e que tudo sobe/desce como um grupo coerente.

Para este projeto, isto é especialmente relevante porque a arquitetura
assenta em **componentes agnósticos que comunicam por um contrato
explícito** — o Compose reforça essa fronteira: cada peça de infra é
um container isolado, com a sua própria versão fixa, e os componentes
da aplicação (`Ingestion/`, `Api/`, `Platform/`) só lhes acedem pela
rede, nunca por acesso direto ao processo.

## Containers usados

| Container | Papel | Fase (ver [[Roadmap]]) | Documentação |
|---|---|---|---|
| **Mosquitto** | Broker MQTT — recebe as leituras publicadas pelos ESP32 (ou pelo simulador) e distribui-as ao Ingestion Service | 2–3 | [mosquitto.org/documentation](https://mosquitto.org/documentation/) |
| **Postgres** | *Last value* de cada sensor — o estado atual que a Api serve ao dashboard | 4 | [postgresql.org/docs](https://www.postgresql.org/docs/16/) |
| **ClickHouse** | Histórico de séries temporais — alimenta os gráficos do dashboard | 7 | [clickhouse.com/docs](https://clickhouse.com/docs) |
| **Prometheus** | Recolhe métricas expostas pela Api/Ingestion | 9 | [prometheus.io/docs](https://prometheus.io/docs/introduction/overview/) |
| **Grafana** | Dashboards sobre as métricas do Prometheus | 9 | [grafana.com/docs](https://grafana.com/docs/grafana/latest/) |

`Ingestion/`, `Api/` e `Platform/` não estão no compose — correm
localmente (`go run`, `./mvnw quarkus:dev`, `ng serve`) para manter
hot-reload rápido durante o desenvolvimento. Passar a corrê-los também
em container é uma opção a considerar mais tarde (Fase 8/9), quando o
objetivo passar a ser testar o sistema como um todo em vez de iterar
rápido num componente.

## Decisão: subir por profile, não tudo de uma vez

O `docker-compose.yaml` agrupa os serviços em `profiles` (`mqtt`,
`postgres`, `clickhouse`, `observability`, `full`), para que o ambiente
local acompanhe a fase do roadmap em que se está — não faz sentido ter
o ClickHouse a correr enquanto ainda se trabalha na Fase 2. Ver
`Deployment/Local/README.md` para a lista de comandos por profile.

## Ver também

- [[Contrato de Dados]] — schema/tópicos que ligam ESP32 → Ingestion → Api.
- [[Ingestion Service (Go)]] — o consumidor do Mosquitto.
- [[Ports and Adapters (Arquitetura Hexagonal)]] — o padrão usado no
  Ingestion Service, que também motiva manter a infra como containers
  substituíveis atrás de uma interface clara.
