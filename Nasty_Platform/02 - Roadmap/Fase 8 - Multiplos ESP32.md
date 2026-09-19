---
tags: [roadmap, fase]
---

# Fase 8 — Múltiplos ESP32

**Tag:** `v8.0.0` · **Depende de:** [[Fase 7 - ClickHouse e Historico]]

## Objetivo
Provar a agnosticidade da arquitetura: vários ESP32 reais (com sensores iguais ou diferentes) a publicar em paralelo, geridos pelo mesmo pipeline sem alterações de código fora do wiring por dispositivo.

## Tasks
- [ ] Flashar ≥2 ESP32 com `deviceId` diferentes (e, idealmente, sensores diferentes implementando `ISensor`).
- [ ] Registo de devices: decidir se existe uma tabela `devices` (nome, localização, tipo) na API ou se é implícito pelos dados recebidos.
- [ ] Dashboard: listar/filtrar por device.
- [ ] Validar que adicionar um novo sensor só implica: (1) nova classe `ISensor`, (2) wiring no `main.c` do device — nada nas outras camadas.
- [ ] Introduzir atualização **OTA** do firmware (deixa de ser preciso acesso físico/USB a cada dispositivo) — ver [[Esp32 - OTA (Atualizacoes Over-The-Air)]] para o design e as tasks detalhadas.

## Componentes envolvidos
- [[Esp32 - Firmware]]
- [[Esp32 - OTA (Atualizacoes Over-The-Air)]]
- [[Api (Quarkus)]]
- [[Platform (Dashboard Angular)]]

## Definição de pronto
Dois ou mais dispositivos físicos reportam em simultâneo e aparecem distintamente no dashboard.

## Próxima fase
[[Fase 9 - Observabilidade e Resiliencia]]
