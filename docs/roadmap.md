# Roadmap — Fases, Tasks, Releases e Tags

> **O roadmap detalhado (objetivo, tasks e definição de pronto por fase) mudou-se para o vault Obsidian: [`Vault/02 - Roadmap/Roadmap.md`](../Vault/02%20-%20Roadmap/Roadmap.md).** Este ficheiro mantém apenas a convenção de release/tag, que é transversal a todas as fases.

---

## Convenção de Release e Tag

- **Cada fase = uma release major** (`v1.0.0`, `v2.0.0`, ...).
- A tag é criada na branch principal **somente depois** que todas as tasks da fase estiverem concluídas e o PR/merge aprovado.
- Formato da tag: `v<MAJOR>.<MINOR>.<PATCH>` (SemVer). Usamos `MAJOR` para indicar a fase.
- **Hotfixes** dentro de uma fase já liberada usam `PATCH` (`v1.0.1`, `v1.0.2`), sem criar nova fase.

### Como liberar uma fase (fluxo)

```bash
# 1. Merge do PR da fase na branch principal (master)
# 2. Criar e enviar a tag:
git tag -a v1.0.0 -m "Fase 1: <título da fase>"
git push origin v1.0.0
# 3. Criar a release:
gh release create v1.0.0 --title "Fase 1: <título da fase>" --notes "O que foi entregue nesta fase..."
```

> Alternativa sem `gh`: criar a release pela UI do GitHub, apontando para a tag criada.

### Checklist de conclusão de fase (Definition of Done)

- [ ] Todas as tasks da fase concluídas (ver a nota da fase no vault).
- [ ] Build/lint/testes passando nos componentes envolvidos.
- [ ] PR revisado e mergeado na branch principal.
- [ ] Tag `vX.0.0` criada e enviada.
- [ ] Release publicada com descrição do que foi entregue.

---

## Resumo das releases

| Fase | Entrega | Tag | Nota no vault |
|---|---|---|---|
| 0 | Baseline do scaffold | `v0.1.0` | [[Fase 0 - Baseline do Scaffold]] |
| 1 | Núcleo agnóstico do firmware ESP32 | `v1.0.0` | [[Fase 1 - Nucleo Agnostico do Firmware]] |
| 2 | Sensor real + publish MQTT | `v2.0.0` | [[Fase 2 - Sensor e MQTT no Firmware]] |
| 3 | Broker MQTT + Ingestion Service (Go) | `v3.0.0` | [[Fase 3 - Broker MQTT e Ingestion Service]] |
| 4 | API Quarkus + Postgres | `v4.0.0` | [[Fase 4 - API Quarkus]] |
| 5 | Dashboard Angular + polling | `v5.0.0` | [[Fase 5 - Dashboard Angular Polling]] |
| 6 | Tempo real (SSE/WebSocket) | `v6.0.0` | [[Fase 6 - Tempo Real (SSE-WebSocket)]] |
| 7 | ClickHouse + histórico | `v7.0.0` | [[Fase 7 - ClickHouse e Historico]] |
| 8 | Múltiplos ESP32 | `v8.0.0` | [[Fase 8 - Multiplos ESP32]] |
| 9 | Observabilidade + resiliência | `v9.0.0` | [[Fase 9 - Observabilidade e Resiliencia]] |

Todos os itens "Nota no vault" são links wiki (`[[...]]`) — abrem no Obsidian a partir de `Vault/`. Fora do Obsidian, navegue diretamente para `Vault/02 - Roadmap/<nome da fase>.md`.
