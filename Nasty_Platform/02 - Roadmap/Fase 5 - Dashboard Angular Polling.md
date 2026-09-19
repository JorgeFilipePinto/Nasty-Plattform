---
tags: [roadmap, fase]
---

# Fase 5 — Dashboard Angular (Polling)

**Tag:** `v5.0.0` · **Depende de:** [[Fase 4 - API Quarkus]]

## Objetivo
Dashboard Angular a consumir `GET /readings/latest` com polling simples (`setInterval`).

## Tasks
- [ ] Criar projeto Angular em `Platform/`.
- [ ] Service dedicado a chamar a API (URL via `environment.ts`).
- [ ] Componente de dashboard: lista de devices/sensores com o último valor.
- [ ] Polling com `setInterval` (intervalo configurável).
- [ ] Tratamento de erro/estado de carregamento (API em baixo, sem dados ainda).

## Componentes envolvidos
- [[Platform (Dashboard Angular)]]

## Definição de pronto
Abrir o dashboard mostra os valores atuais de todos os devices, atualizando a cada N segundos.

## Próxima fase
[[Fase 6 - Tempo Real (SSE-WebSocket)]]
