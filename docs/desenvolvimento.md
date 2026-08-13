# Guia de Trabalho e Desenvolvimento

Guia de referência para quem for trabalhar neste repositório. Cobre pré-requisitos, fluxo de trabalho, comandos esperados por componente e convenções do projeto.

> **Estado atual:** o repositório é um scaffold vazio. Este guia documenta o setup e o fluxo *planejados* para cada stack. À medida que cada componente for implementado, atualize os comandos aqui e no `AGENTS.md` com o que realmente funciona.

## Índice

1. [Visão geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Setup inicial](#setup-inicial)
4. [Desenvolvimento por componente](#desenvolvimento-por-componente)
5. [Workflow Git](#workflow-git)
6. [Qualidade de código](#qualidade-de-código)
7. [Executando tudo localmente](#executando-tudo-localmente)
8. [Mapa de documentação](#mapa-de-documentação)

---

## Visão geral

Plataforma IoT de aprendizado com quatro partes:

| Pasta | Componente | Stack |
|---|---|---|
| `Esp32/` | Firmware do dispositivo | ESP-IDF (C/C++/CMake) |
| `Api/` | Backend | Spring Boot (Java) |
| `Platform/` | Dashboard | Angular |
| `Deployment/` | Infra local | Docker Compose |

O roadmap em fases está no `README.md`. Trabalhe nas fases em ordem — cada uma depende da anterior.

---

## Pré-requisitos

### Gerais

- **Docker** — para os serviços locais (Postgres, MQTT broker, ClickHouse, Prometheus).
- **Git** — fluxo de trabalho padrão com branches e pull requests.

### ESP32

- **ESP-IDF** (recomendado: instalar via `idf.py` a partir do esp-idf de master ou stable, ou via plugin do VSCode/PlatformIO).
- A variável de ambiente do ESP-IDF deve estar carregada (`source export.sh` ou `idf.py` no PATH) antes de build/flash.

### Api (Spring Boot)

- **JDK 17+** (Java LTS).
- **Maven** (`mvn`) ou o **Maven wrapper** (`./mvnw`) que será adicionado ao repo — prefira o wrapper quando disponível.

### Platform (Angular)

- **Node.js LTS**.
- **Angular CLI** (`npm install -g @angular/cli`) — ou use `npx @angular/cli` para evitar instalação global.

---

## Setup inicial

```bash
# 1. Clone e instale as ferramentas do stack desejado (ver Pré-requisitos)
# 2. Suba os serviços de infraestrutura:
docker compose -f Deployment/Local/docker-compose.yaml up -d

# 3. Configure cada componente (ver abaixo)
```

---

## Desenvolvimento por componente

### Esp32/

Projeto ESP-IDF. Siga o padrão de build CMake do ESP-IDF — **não commite arquivos gerados** (`build/` e outros artefatos já estão no `.gitignore`).

```bash
# Configurar ambiente do ESP-IDF (uma vez por sessão)
source $IDF_PATH/export.sh

# Build
idf.py build

# Flash + monitor serial
idf.py -p /dev/ttyUSB0 flash monitor

# Menus de configuração
idf.py menuconfig
```

**Convenções:**
- Mantenha o diretório `Esp32/` como raiz do projeto ESP-IDF, sem arquivos gerados na raiz do repo.
- Toda comunicação com a API deve ter o payload JSON documentado (endpoint, campos, tipos).

### Api/

Backend Spring Boot. Estrutura padrão do Maven: `src/main/java`, `src/main/resources`, `src/test/java`.

```bash
# Rodar a aplicação
mvn spring-boot:run
# ou, com o wrapper
./mvnw spring-boot:run

# Rodar apenas um teste
mvn test -Dtest=NomeDaClasseTest

# Rodar todos os testes
mvn test

# Empacotar (gera jar em target/)
mvn clean package
```

**Convenções:**
- Endpoints REST com validação de entrada (`@Valid` + `jakarta.validation`).
- Postgres usado para o *last value*; migrations versionadas (Flyway/Liquibase) quando forem introduzidas.
- Novos endpoints devem vir acompanhados de testes.
- Fases avançadas: SSE/WebSocket e Actuator + Prometheus.

### Platform/

Frontend Angular. Estrutura gerada pelo Angular CLI.

```bash
# Instalar dependências (na primeira vez)
npm install

# Servidor de desenvolvimento
ng serve

# Build de produção
ng build

# Testes unitários
ng test

# Lint
ng lint
```

**Convenções:**
- Consumo da API via um service dedicado (não espalhar chamadas HTTP pelos componentes).
- Fase inicial: polling com `setInterval`; substituir por WebSocket/SSE quando a fase 4 chegar.
- Dados de ambiente (URL da API) via environment files do Angular, nunca hardcoded.

### Deployment/Local/

`docker-compose.yaml` centraliza os serviços locais. Adicione aqui: Postgres, broker MQTT (ex.: Mosquitto), ClickHouse e Prometheus à medida que as fases avançadas entrarem.

```bash
docker compose -f Deployment/Local/docker-compose.yaml up -d   # subir
docker compose -f Deployment/Local/docker-compose.yaml down     # derrubar
docker compose -f Deployment/Local/docker-compose.yaml logs -f  # logs
```

---

## Workflow Git

- Trabalhe em **branches** (ex.: `feat/fase-2-api`, `fix/x`) e abra **pull requests** — nunca commite direto em `master`.
- **Commits pequenos e atômicos**, com mensagens descritivas no padrão do repo.
- **Não commite**:
  - Segredos/credenciais (`.env`, chaves, tokens).
  - Artefatos de build (`target/`, `build/`, `dist/`, `node_modules/`).
- Antes de abrir um PR, confira o `git status`, `git diff` e o histórico recente.

---

## Qualidade de código

| Componente | Comando esperado |
|---|---|
| Api | `mvn test` (testes), checkstyle/spotless se configurado |
| Platform | `ng lint` e `ng test` |
| Esp32 | build do ESP-IDF (`idf.py build`) |

> Regra do projeto: **toda mudança passa por lint/build + testes antes do PR.** Quando uma ferramenta de lint/teste existir de verdade num componente, registre o comando exato no `AGENTS.md`.

---

## Executando tudo localmente

Ordem típica durante o desenvolvimento (exemplo com Docker Compose):

1. Suba a infra: `docker compose -f Deployment/Local/docker-compose.yaml up -d`.
2. Rode a API em `Api/` (`mvn spring-boot:run`).
3. Rode o Angular em `Platform/` (`ng serve`).
4. Flash o firmware no ESP32 (`idf.py flash monitor`).
5. Valide o fluxo: o sensor publica → API ingere → dashboard exibe.

---

## Mapa de documentação

- `README.md` — visão geral, arquitetura, fases de estudo e stack.
- `AGENTS.md` — orientações para sessões de IA/OpenCode no repo (leia antes de codar).
- `docs/desenvolvimento.md` — este guia.
- `docs/roadmap.md` — fases, tasks, critérios de aceite e convenção de releases/tags.
- `Deployment/Local/docker-compose.yaml` — serviços de infraestrutura.
