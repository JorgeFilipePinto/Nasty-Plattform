# Nasty-Plattform

Projeto de aprendizado de uma plataforma IoT de ponta a ponta e, sobretudo, um laboratório de **arquitetura de software** e **skills de desenvolvimento de código**: vários **ESP32** leem sensores e publicam leituras via **MQTT**, um **serviço de ingestão** (Go) valida/normaliza e faz buffer em **SQLite**, uma **API Quarkus** persiste em **Postgres** e **ClickHouse** e serve um **dashboard Angular**.

> 📓 A arquitetura, o roadmap detalhado e as tasks por componente vivem num vault Obsidian em [`Vault/`](Vault/00%20-%20Home.md) — comece por `Vault/00 - Home.md`. Este README é só o resumo.

## Visão geral

A plataforma é um laboratório incremental: cada fase introduz uma nova peça de arquitetura sobre a anterior, sempre com o mesmo princípio — os componentes são **agnósticos** entre si (comunicam através de interfaces e de um contrato de dados explícito), só a implementação concreta de cada sensor é individual por dispositivo.

## Arquitetura

```
┌─────────┐  ┌─────────┐  ┌─────────┐          MQTT           ┌───────────┐
│ ESP32 #1│  │ ESP32 #2│  │ ESP32 #N│ ───────────────────────▶ │  Broker   │
│ (sensor)│  │ (sensor)│  │ (sensor)│                          │ Mosquitto │
└─────────┘  └─────────┘  └─────────┘                          └─────┬─────┘
                                                                       │ subscribe
                                                                       ▼
                                                        ┌───────────────────────────┐
                                                        │  Ingestion Service (Go)   │
                                                        │  MQTT → valida → SQLite   │
                                                        └─────────────┬─────────────┘
                                                                       │ HTTP forward
                                                                       ▼
                                                        ┌───────────────────────────┐
                                                        │       API (Quarkus)       │
                                                        │  REST + Postgres +        │
                                                        │  ClickHouse (histórico)   │
                                                        └─────────────┬─────────────┘
                                                                       │ REST / SSE / WS
                                                                       ▼
                                                        ┌───────────────────────────┐
                                                        │   Dashboard (Angular)     │
                                                        └───────────────────────────┘
```

Ver o diagrama completo (mermaid) e o detalhe de cada seta em [`Vault/01 - Arquitetura/Arquitetura Geral.md`](Vault/01%20-%20Arquitetura/Arquitetura%20Geral.md).

### Componentes

- **`Esp32/`** — Firmware ESP-IDF (C/C++/CMake). Núcleo agnóstico (Wi-Fi, scheduler, cliente MQTT) + sensores atrás da interface `ISensor` (já existe em `Esp32/components/sensors/`). Publica leituras em MQTT.
- **`Ingestion/`** (planeado) — Serviço em Go: subscreve o broker MQTT, valida/normaliza as leituras, grava-as num buffer local SQLite e encaminha-as para a API, com retry se esta estiver indisponível.
- **`Api/`** — Backend, a migrar de Spring Boot para **Quarkus** (Java). Recebe leituras do `Ingestion/`, persiste o *last value* no Postgres e o histórico no ClickHouse, serve o dashboard (REST, depois SSE/WebSocket).
- **`Platform/`** — Frontend Angular. Consome a API inicialmente com polling simples (`setInterval`), evoluindo para atualização em tempo real via WebSocket/SSE, e gráficos de série temporal do ClickHouse.
- **`Deployment/Local/`** — `docker-compose.yaml` para subir os serviços locais (Mosquitto, Postgres, ClickHouse, Prometheus, etc.).

## Estrutura do repositório

```
Nasty-Plattform/
├── Api/                    # Backend (a migrar de Spring Boot para Quarkus)
├── Esp32/                  # Firmware ESP32 (ESP-IDF, C/C++/CMake)
├── Ingestion/               # Serviço de ingestão MQTT → SQLite → forward (Go, planeado)
├── Platform/                # Dashboard Angular
├── Deployment/
│   └── Local/
│       └── docker-compose.yaml
├── Vault/                   # Vault Obsidian: arquitetura, roadmap, tasks (comece em "00 - Home.md")
├── docs/                    # Guia de setup/comandos por componente
├── AGENTS.md
└── README.md
```

## Fases de estudo

O projeto é conduzido em fases, cada uma construindo sobre a anterior. A tabela completa, com objetivo, tasks e definição de pronto de cada fase, está em [`Vault/02 - Roadmap/Roadmap.md`](Vault/02%20-%20Roadmap/Roadmap.md).

| Fase | Entrega |
|---|---|
| 0 | Baseline do scaffold (repo, docs, vault) |
| 1 | Núcleo agnóstico do firmware ESP32 (Wi-Fi, scheduler, `ISensor`) |
| 2 | Sensor de temperatura/humidade real + publish MQTT |
| 3 | Broker MQTT + Ingestion Service (Go) grava SQLite |
| 4 | API Quarkus recebe do Ingestion Service, persiste Postgres |
| 5 | Dashboard Angular com polling |
| 6 | Tempo real (SSE/WebSocket) |
| 7 | ClickHouse + histórico + gráficos de série temporal |
| 8 | Múltiplos ESP32 reais em paralelo |
| 9 | Observabilidade (Prometheus/Grafana) + resiliência |
| Extra (não prioritário) | Deploy em produção: domínio+VPS+NGINX, ou alternativa VPN (WireGuard) |

## Stack

| Componente | Tecnologia |
|---|---|
| Firmware | ESP32 com ESP-IDF (C/C++/CMake) |
| Transporte | MQTT (Mosquitto) |
| Ingestão | Go, SQLite (buffer local) |
| API | Quarkus (Java), Postgres, ClickHouse |
| Frontend | Angular |
| Deploy local | Docker Compose |
| Observabilidade (avançado) | Actuator/Micrometer, Prometheus, Grafana, Thanos |

## Status

Fresh scaffold — nenhum componente implementado ainda (interface `ISensor` e scaffold Spring Boot do `Api/` já existem como ponto de partida). Consulte `AGENTS.md` para a estrutura do repositório e `Vault/00 - Home.md` para a arquitetura e as tasks detalhadas.
