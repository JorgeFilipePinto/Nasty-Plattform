---
tags: [roadmap, fase]
---

# Fase 1 — Núcleo Agnóstico do Firmware

**Tag:** `v1.0.0` · **Depende de:** [[Fase 0 - Baseline do Scaffold]]

## Objetivo
Construir a parte do firmware que **não** depende do sensor: ligação Wi-Fi, configuração do dispositivo (deviceId, intervalo de leitura) e um scheduler que chama periodicamente `ISensor::read()`. Sem MQTT ainda — validar por log série.

## Porquê nesta ordem
Isto força o esqueleto agnóstico a existir e ser testado **antes** de qualquer sensor real ou transporte, provando a separação descrita em [[Principios de Design]].

## Tasks
- [ ] Configurar Wi-Fi (SSID/senha via `idf.py menuconfig` ou `Kconfig.projbuild`).
- [ ] Definir `DeviceConfig` (deviceId, intervalo de leitura) — de onde vem: hardcoded, NVS, ou Kconfig?
- [ ] Implementar um "device loop" agnóstico que recebe um `ISensor*` (ou lista) e chama `read()` no intervalo configurado.
- [ ] Logar (`printf`/`ESP_LOG*`) o `SensorData` lido, sem publicar ainda.
- [ ] Validar com `idf.py flash monitor` (ou com um sensor "fake" que devolve valores fixos, para não bloquear em hardware).

## Componentes envolvidos
- [[Esp32 - Firmware]]

## Conceitos relevantes
- [[Interfaces e Abstracao]]

## Definição de pronto
`idf.py build` passa; no monitor série vê-se o loop a chamar `read()` no intervalo certo, usando só a interface `ISensor` (zero referências a um sensor concreto fora do ponto de wiring em `main.c`).

## Próxima fase
[[Fase 2 - Sensor e MQTT no Firmware]]
