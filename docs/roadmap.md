# Roadmap — Fases, Tasks, Releases e Tags

Este documento divide o projeto em fases, cada uma com suas tasks e critérios de aceite. **Cada fase concluída vira uma release**, representada por uma **tag de versão** no Git.

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
git tag -a v1.0.0 -m "Fase 1: ESP32 → HTTP"
git push origin v1.0.0
# 3. Criar a release:
gh release create v1.0.0 --title "Fase 1: ESP32 → HTTP" --notes "O que foi entregue nesta fase..."
```

> Alternativa sem `gh`: criar a release pela UI do GitHub, apontando para a tag criada.

### Checklist de conclusão de fase (Definition of Done)

- [ ] Todas as tasks da fase concluídas.
- [ ] Build/lint/testes passando nos componentes envolvidos.
- [ ] PR revisado e mergeado na branch principal.
- [ ] Tag `vX.0.0` criada e enviada.
- [ ] Release publicada com descrição do que foi entregue.

---

## Fase 0 — Baseline do Scaffold

**Objetivo:** repositório estruturado com layout de pastas, `.gitignore`, README e docs.

**Tasks:**
- [ ] Estrutura de pastas (`Api/`, `Esp32/`, `Platform/`, `Deployment/`).
- [ ] `.gitignore` cobrindo C/C++, Java/Spring Boot, Node/Angular e IDE/OS.
- [ ] README com visão geral, arquitetura e fases.
- [ ] Guias de desenvolvimento e este roadmap.
- [ ] `AGENTS.md` com orientações de trabalho.

**Release:** `v0.1.0`

---

## Fase 1 — ESP32 → HTTP

**Objetivo:** firmware ESP32 lendo um sensor e enviando `POST` HTTP com JSON.

**Tasks:**
- [x] Criar projeto ESP-IDF em `Esp32/`.
- [x] Configurar Wi-Fi (SSID/senha via `idf.py menuconfig`).
- [x] Implementar leitura do sensor de temperatura interno do chip.
- [x] Implementar cliente HTTP montando payload JSON.
- [x] Enviar `POST` para a API em intervalo definido (endpoint configurável).
- [ ] Validar o envio apontando o endpoint para o mock local (`Deployment/Local/mock_api.py`) com `idf.py flash monitor`.

**Release:** `v1.0.0`

---

## Fase 2 — Spring Boot API

**Objetivo:** endpoint REST com validação, Postgres para *last value* e testes.

**Tasks:**
- [ ] Criar projeto Spring Boot em `Api/` (JDK 17+, Maven/wrapper).
- [ ] Modelo `SensorReading` (deviceId, valor, timestamp).
- [ ] `POST /readings` com validação de entrada (`@Valid`).
- [ ] Persistência do *last value* no Postgres (chave por `deviceId`).
- [ ] `GET /readings/latest` para consultar o último valor.
- [ ] Postgres no `Deployment/Local/docker-compose.yaml`.
- [ ] Migrations versionadas (Flyway/Liquibase).
- [ ] Testes unitários e de integração.

**Release:** `v2.0.0`

---

## Fase 3 — Angular + Polling

**Objetivo:** dashboard Angular consumindo a API com polling simples (`setInterval`).

**Tasks:**
- [ ] Criar projeto Angular em `Platform/`.
- [ ] Service de dados consumindo a API (URL via environment).
- [ ] Componente de dashboard exibindo o último valor lido.
- [ ] Polling com `setInterval` para atualização periódica.
- [ ] Tratamento de erro/estado de carregamento.

**Release:** `v3.0.0`

---

## Fase 4 — Tempo Real

**Objetivo:** substituir polling por WebSocket/SSE para atualização em tempo real.

**Tasks:**
- [ ] Expor evento SSE (ou WebSocket) no Spring Boot ao receber nova leitura.
- [ ] Angular consumindo SSE/WebSocket e atualizando o dashboard.
- [ ] Remover o polling (`setInterval`).
- [ ] Validar atualização em tempo real de ponta a ponta.

**Release:** `v4.0.0`

---

## Fase 5 — MQTT

**Objetivo:** MQTT como transporte alternativo de ingestão de dados.

**Tasks:**
- [ ] Broker MQTT (Mosquitto) no `docker-compose.yaml`.
- [ ] Firmware publicando leituras em tópico MQTT.
- [ ] Spring Boot consumindo do broker (subscription) e persistindo.
- [ ] Definir se MQTT substitui ou coexiste com o HTTP.

**Release:** `v5.0.0`

---

## Fase 6 — ClickHouse

**Objetivo:** histórico de dados e gráficos de série temporal no dashboard.

**Tasks:**
- [ ] ClickHouse no `docker-compose.yaml`.
- [ ] Ingestão do histórico das leituras para o ClickHouse.
- [ ] Endpoint de séries temporais (range de tempo) na API.
- [ ] Gráficos de série temporal no dashboard Angular.

**Release:** `v6.0.0`

---

## Fase 7 — Observabilidade

**Objetivo:** métricas do Spring Boot (Actuator + Prometheus); Thanos opcional.

**Tasks:**
- [ ] Actuator + `micrometer-registry-prometheus` na API.
- [ ] Prometheus no `docker-compose.yaml` coletando da API.
- [ ] Grafana (ou dashboards) com métricas básicas.
- [ ] (Opcional) Thanos para retenção/escala de métricas.

**Release:** `v7.0.0`

---

## Resumo das releases

| Fase | Entrega | Tag | Status |
|---|---|---|---|
| 0 | Baseline do scaffold | `v0.1.0` | Não liberada |
| 1 | ESP32 → HTTP | `v1.0.0` | Não liberada |
| 2 | Spring Boot API | `v2.0.0` | Não liberada |
| 3 | Angular + polling | `v3.0.0` | Não liberada |
| 4 | Tempo real (SSE/WebSocket) | `v4.0.0` | Não liberada |
| 5 | MQTT | `v5.0.0` | Não liberada |
| 6 | ClickHouse | `v6.0.0` | Não liberada |
| 7 | Observabilidade | `v7.0.0` | Não liberada |
