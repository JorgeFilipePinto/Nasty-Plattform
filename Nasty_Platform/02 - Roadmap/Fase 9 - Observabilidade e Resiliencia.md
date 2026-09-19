---
tags: [roadmap, fase]
---

# Fase 9 — Observabilidade e Resiliência

**Tag:** `v9.0.0` · **Depende de:** [[Fase 8 - Multiplos ESP32]]

## Objetivo
Fechar o laboratório com métricas, resiliência a falhas e testes de carga — a parte "produção" do exercício.

## Tasks
- [ ] Actuator/Micrometer equivalente no Quarkus (`quarkus-micrometer-registry-prometheus`).
- [ ] Prometheus no `docker-compose.yaml` a fazer scrape da API e (se possível) do Ingestion Service.
- [ ] Grafana com dashboards básicos (latência, taxa de mensagens, erros).
- [ ] Ingestion Service: retry/backoff testado (matar a API a propósito e confirmar que o SQLite acumula e reenvia depois).
- [ ] Teste de carga simples (ex.: simulador a publicar a alta frequência) para ver onde o pipeline degrada primeiro.
- [ ] (Opcional) Thanos para retenção/escala de métricas.

## Componentes envolvidos
- Todos.

## Conceitos relevantes
- [[Estrategia de Testes]]

## Definição de pronto
Desligar a API por 1 minuto e voltar a ligar não perde dados (o Ingestion Service reenvia o que ficou pendente no SQLite); dashboards de métricas mostram atividade real.
