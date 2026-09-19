---
tags: [roadmap, fase]
---

# Fase 3 — Broker MQTT e Ingestion Service

**Tag:** `v3.0.0` · **Depende de:** [[Fase 2 - Sensor e MQTT no Firmware]]

## Objetivo
Subir um broker MQTT (Mosquitto) via Docker Compose e criar o `Ingestion Service` em Go: subscreve o broker, valida o payload e grava em SQLite. **Sem** encaminhar para a API ainda — isso é a Fase 4.

## Tasks
- [ ] Adicionar Mosquitto ao `Deployment/Local/docker-compose.yaml`.
- [ ] Criar módulo Go em `Ingestion/`.
- [ ] Definir interface `Subscriber` (implementação MQTT) — ver [[Ports and Adapters (Arquitetura Hexagonal)]].
- [ ] Definir interface `Storage` (implementação SQLite) com o schema de [[Contrato de Dados]].
- [ ] Processamento: validar payload, normalizar, gravar.
- [ ] Testes unitários do processamento sem depender de um broker real (mock do `Subscriber`).

## Componentes envolvidos
- [[Ingestion Service (Go)]]
- [[Deployment (Docker Compose)]]

## Conceitos relevantes
- [[MQTT - Conceitos]]
- [[SQLite como Buffer Local]]
- [[Ports and Adapters (Arquitetura Hexagonal)]]

## Definição de pronto
Com o firmware (ou um simulador) a publicar, as linhas aparecem na tabela `readings` do SQLite local do Ingestion Service.

## Próxima fase
[[Fase 4 - API Quarkus]]
