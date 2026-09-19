---
tags: [roadmap, fase]
---

# Fase 4 — API Quarkus

**Tag:** `v4.0.0` · **Depende de:** [[Fase 3 - Broker MQTT e Ingestion Service]]

## Objetivo
Migrar `Api/` de Spring Boot para Quarkus, expor um endpoint para receber leituras do Ingestion Service e persistir o *last value* em Postgres. O Ingestion Service passa a encaminhar (forward) o que grava em SQLite.

## Tasks
- [ ] Recriar o scaffold de `Api/` como projeto Quarkus (Maven, `quarkus-resteasy-reactive`, `quarkus-jdbc-postgresql`, `quarkus-hibernate-orm-panache` ou `quarkus-jdbc` puro — decidir em [[Api (Quarkus)]]).
- [ ] `POST /readings` com validação de entrada, conforme [[Contrato de Dados]].
- [ ] Persistência do last value no Postgres (chave `deviceId` + `sensorType`).
- [ ] `GET /readings/latest` (todos os devices) e `GET /readings/latest/{deviceId}`.
- [ ] Postgres no `docker-compose.yaml`.
- [ ] Migrations versionadas (Flyway).
- [ ] Testes (`@QuarkusTest`) de unidade e integração.
- [ ] `Ingestion Service`: implementar `Forwarder` (HTTP client) com retry para linhas não enviadas (`forwarded = false`).

## Componentes envolvidos
- [[Api (Quarkus)]]
- [[Ingestion Service (Go)]]

## Conceitos relevantes
- [[Postgres vs ClickHouse]]
- [[Estrategia de Testes]]

## Definição de pronto
Fim-a-fim: ESP32 → MQTT → Ingestion (SQLite) → API (Postgres). `GET /readings/latest` devolve o último valor real.

## Próxima fase
[[Fase 5 - Dashboard Angular Polling]]
