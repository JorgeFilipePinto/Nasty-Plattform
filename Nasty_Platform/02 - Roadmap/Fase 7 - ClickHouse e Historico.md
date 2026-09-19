---
tags: [roadmap, fase]
---

# Fase 7 — ClickHouse e Histórico

**Tag:** `v7.0.0` · **Depende de:** [[Fase 6 - Tempo Real (SSE-WebSocket)]]

## Objetivo
Guardar todo o histórico de leituras (não só o last value) em ClickHouse e expor gráficos de série temporal no dashboard.

## Tasks
- [ ] ClickHouse no `docker-compose.yaml`.
- [ ] API: escrever cada leitura recebida também em ClickHouse (append-only), além do upsert no Postgres.
- [ ] Endpoint de série temporal (`GET /readings/history?deviceId=&sensorType=&from=&to=`).
- [ ] Angular: componente de gráfico (biblioteca a escolher) a consumir o endpoint de histórico.

## Componentes envolvidos
- [[Api (Quarkus)]]
- [[Platform (Dashboard Angular)]]
- [[Deployment (Docker Compose)]]

## Conceitos relevantes
- [[Postgres vs ClickHouse]]

## Definição de pronto
O dashboard mostra um gráfico de série temporal de, pelo menos, um sensor, com dados reais das últimas horas.

## Próxima fase
[[Fase 8 - Multiplos ESP32]]
