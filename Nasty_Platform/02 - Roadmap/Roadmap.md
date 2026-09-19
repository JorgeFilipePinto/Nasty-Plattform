---
tags: [roadmap]
---

# Roadmap

Convenção de release: cada fase = 1 release major (`vX.0.0`), tag criada só depois de todas as tasks da fase estarem concluídas e o PR mergeado. Hotfixes dentro de uma fase usam `PATCH` (`vX.0.1`).

```bash
git tag -a v1.0.0 -m "Fase 1: <titulo>"
git push origin v1.0.0
gh release create v1.0.0 --title "Fase 1: <titulo>" --notes "..."
```

## Fases

| Fase | Nota | Objetivo resumido | Tag |
|---|---|---|---|
| 0 | [[Fase 0 - Baseline do Scaffold]] | Estrutura do repo, docs, vault | `v0.1.0` |
| 1 | [[Fase 1 - Nucleo Agnostico do Firmware]] | Firmware ESP32: Wi-Fi + scheduler + interface de sensor, sem transporte ainda | `v1.0.0` |
| 2 | [[Fase 2 - Sensor e MQTT no Firmware]] | Sensor de temperatura/humidade real + publish MQTT | `v2.0.0` |
| 3 | [[Fase 3 - Broker MQTT e Ingestion Service]] | Broker Mosquitto + Ingestion Service (Go) grava SQLite | `v3.0.0` |
| 4 | [[Fase 4 - API Quarkus]] | API Quarkus recebe do Ingestion, persiste Postgres | `v4.0.0` |
| 5 | [[Fase 5 - Dashboard Angular Polling]] | Dashboard Angular com polling | `v5.0.0` |
| 6 | [[Fase 6 - Tempo Real (SSE-WebSocket)]] | Substituir polling por SSE/WebSocket | `v6.0.0` |
| 7 | [[Fase 7 - ClickHouse e Historico]] | Histórico e gráficos de série temporal | `v7.0.0` |
| 8 | [[Fase 8 - Multiplos ESP32]] | Vários dispositivos reais em paralelo + registo de devices | `v8.0.0` |
| 9 | [[Fase 9 - Observabilidade e Resiliencia]] | Métricas, retries, testes de carga | `v9.0.0` |
| Extra (não prioritário) | [[Deploy em Producao - Visao Geral]] | Domínio+VPS+NGINX, ou VPN WireGuard, para acesso fora da rede local | — |

## Definition of Done por fase
- [ ] Todas as tasks da nota da fase concluídas.
- [ ] Build/lint/testes a passar nos componentes envolvidos.
- [ ] PR revisto e mergeado em `master`.
- [ ] Tag `vX.0.0` criada e release publicada.

## Ver também
- [[Arquitetura Geral]]
