---
tags: [roadmap, fase]
---

# Fase 2 — Sensor e MQTT no Firmware

**Tag:** `v2.0.0` · **Depende de:** [[Fase 1 - Nucleo Agnostico do Firmware]]

## Objetivo
Implementar `TempSensor` (DHT, temperatura + humidade) a sério e publicar cada leitura via MQTT, seguindo o [[Contrato de Dados]].

## Tasks
- [ ] Completar `DHT_sensor.cpp` (leitura real do pino, sem valores fixos).
- [ ] Adicionar cliente MQTT ao componente `wifi` (ou um novo componente `mqtt`, agnóstico — não sabe nada de sensores).
- [ ] Montar o payload JSON conforme [[Contrato de Dados]] a partir de `SensorData` + `DeviceConfig`.
- [ ] Publicar no tópico `nasty/<deviceId>/<sensorType>`.
- [ ] Validar fim-a-fim com um broker local (`mosquitto_sub` na linha de comandos) antes de o Ingestion Service existir.

## Componentes envolvidos
- [[Esp32 - Firmware]]

## Conceitos relevantes
- [[MQTT - Conceitos]]
- [[Contrato de Dados]]

## Definição de pronto
`mosquitto_sub -t 'nasty/#' -v` mostra leituras reais de temperatura/humidade chegando no intervalo configurado.

## Próxima fase
[[Fase 3 - Broker MQTT e Ingestion Service]]
