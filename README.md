# Nasty-Plattform

Projeto de aprendizado de uma plataforma IoT de ponta a ponta: um dispositivo **ESP32** lê sensores e publica os dados, uma **API Spring Boot** ingere e armazena, e um dashboard **Angular** consome os dados em tempo real. O roadmap evolui de HTTP simples até transporte MQTT, histórico com ClickHouse e observabilidade com Prometheus + Thanos.

## Visão geral

A plataforma é um laboratório incremental: cada fase introduz uma nova peça de arquitetura sobre a anterior. Começa com o caminho mais simples possível (sensor → POST HTTP → banco → dashboard com polling) e evolui para comunicação em tempo real, transporte alternativo e análises de série temporal.

## Arquitetura

```
                 HTTP POST (JSON)
┌─────────┐   ┌────────────────────────────────────┐   ┌──────────────┐
│ ESP32   │──▶│           Spring Boot API          │──▶│   Postgres   │
│ (sensor)│   │  REST + validação + teste          │   │ (last value) │
└─────────┘   └────────────────────────────────────┘   └──────────────┘
                     ▲                  │
        polling /    │                  │ SSE / WebSocket
        WebSocket    │                  ▼
        (SSE)        │            ┌──────────────┐
                     └────────────│   Angular    │
                                 └──────────────┘

   Opcional (fases avançadas):
   ┌─────────┐  MQTT   ┌───────┐   ┌──────────────┐   ┌───────────────────┐
   │ ESP32   │────────▶│ Broker│──▶│  ClickHouse  │──▶│  Grafana / charts │
   └─────────┘         └───────┘   │ (histórico)  │   └───────────────────┘
                                   └──────────────┘
   Métricas Spring Boot → Actuator → Prometheus → (opcional) Thanos
```

### Componentes

- **`Esp32/`** — Firmware ESP-IDF (C/C++/CMake). Lê o sensor e envia um POST HTTP com payload JSON; fases avançadas passam a usar MQTT como transporte.
- **`Api/`** — Backend Spring Boot (Java). Expõe endpoint REST com validação, persiste o *last value* no Postgres, possui testes. Fases avançadas adicionam SSE/WebSocket e métricas via Actuator + Prometheus.
- **`Platform/`** — Frontend Angular. Consome a API inicialmente com polling simples (`setInterval`), evoluindo para atualização em tempo real via WebSocket/SSE, e gráficos de série temporal do ClickHouse.
- **`Deployment/Local/`** — `docker-compose.yaml` para subir os serviços locais (Postgres, broker MQTT, ClickHouse, Prometheus, etc.).

## Estrutura do repositório

```
Nasty-Plattform/
├── Api/                    # Backend Spring Boot (Java)
├── Esp32/                  # Firmware ESP32 (ESP-IDF, C/C++/CMake)
├── Platform/               # Dashboard Angular
├── Deployment/
│   └── Local/
│       └── docker-compose.yaml
├── AGENTS.md
└── README.md
```

## Fases de estudo

O projeto é conduzido em fases, cada uma construindo sobre a anterior:

1. **ESP32 → HTTP** — Firmware lendo um sensor e enviando `POST` HTTP com JSON.
2. **Spring Boot básico** — Endpoint REST com validação, Postgres para o *last value*, testes.
3. **Angular + polling** — Dashboard consumindo a API com polling simples (`setInterval`).
4. **Tempo real** — Substituir polling por WebSocket/SSE para atualização em tempo real.
5. **MQTT** — Adicionar MQTT como transporte alternativo para a ingestão de dados.
6. **ClickHouse** — Introduzir ClickHouse para histórico e gráficos de série temporal no dashboard.
7. **Observabilidade** — Métricas do Spring Boot (Actuator + Prometheus); Thanos como próximo passo opcional para escala.

## Stack

| Componente | Tecnologia |
|---|---|
| Firmware | ESP32 com ESP-IDF (C/C++/CMake) |
| API | Spring Boot (Java), Postgres |
| Frontend | Angular |
| Deploy local | Docker Compose |
| Transporte (avançado) | MQTT |
| Histórico (avançado) | ClickHouse |
| Observabilidade (avançado) | Actuator, Prometheus, Thanos |

## Status

Fresh scaffold — nenhum componente implementado ainda. Consulte `AGENTS.md` para a estrutura do repositório e comandos conforme cada parte for criada.
