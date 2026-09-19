---
tags: [roadmap, fase]
---

# Fase 6 — Tempo Real (SSE/WebSocket)

**Tag:** `v6.0.0` · **Depende de:** [[Fase 5 - Dashboard Angular Polling]]

## Objetivo
Substituir o polling por push em tempo real: a API emite um evento assim que recebe uma leitura nova.

## Tasks
- [ ] Escolher SSE ou WebSocket (documentar o porquê em [[Api (Quarkus)]]).
- [ ] API Quarkus: emitir evento ao receber `POST /readings`.
- [ ] Angular: subscrever o stream e atualizar o dashboard sem `setInterval`.
- [ ] Remover o polling.
- [ ] Validar atualização em tempo real de ponta a ponta (ESP32 → ... → dashboard em <1s).

## Componentes envolvidos
- [[Api (Quarkus)]]
- [[Platform (Dashboard Angular)]]

## Definição de pronto
Uma leitura nova aparece no dashboard sem refresh e sem polling ativo.

## Próxima fase
[[Fase 7 - ClickHouse e Historico]]
