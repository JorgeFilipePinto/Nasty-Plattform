---
tags: [arquitetura, contrato]
---

# Contrato de Dados

Define o formato de dados nas fronteiras do sistema. Todas as camadas devem programar contra este contrato (ou uma versão dele), nunca contra detalhes de implementação de outra camada — é o que torna os componentes [[Interfaces e Abstracao|agnósticos]] entre si.

## 1. ESP32 → MQTT (payload publicado)

Tópico (proposta, ajustar em [[Fase 2 - Sensor e MQTT no Firmware]]):
```
nasty/<deviceId>/<sensorType>
```

Payload JSON:
```json
{
  "deviceId": "esp32-01",
  "sensorType": "temperature",
  "value": 23.4,
  "unit": "C",
  "timestamp": 1735000000
}
```

- `deviceId`: identificador único e estável do dispositivo (ex.: derivado do MAC).
- `sensorType`: string livre mas normalizada (ex.: `temperature`, `humidity`) — cada `ISensor` sabe o seu próprio tipo.
- `timestamp`: epoch (segundos). Se o ESP32 não tiver relógio sincronizado (NTP), o serviço de ingestão pode substituir pelo horário de receção — decisão a validar em [[Fase 3 - Broker MQTT e Ingestion Service]].

## 2. Ingestion Service → SQLite (buffer local)

Tabela `readings` (mínimo viável):
| coluna | tipo | notas |
|---|---|---|
| id | INTEGER PK | autoincrement |
| device_id | TEXT | |
| sensor_type | TEXT | |
| value | REAL | |
| unit | TEXT | |
| read_at | INTEGER | epoch, da mensagem MQTT |
| received_at | INTEGER | epoch, quando o ingestion recebeu |
| forwarded | BOOLEAN | default false — usado para retry |

## 3. Ingestion Service → API Quarkus (HTTP POST)

```json
{
  "deviceId": "esp32-01",
  "sensorType": "temperature",
  "value": 23.4,
  "unit": "C",
  "readAt": "2026-09-18T10:00:00Z",
  "receivedAt": "2026-09-18T10:00:01Z"
}
```

Mesmo shape dos dados do SQLite, apenas serializado como ISO-8601 em vez de epoch (decisão a rever, ver nota abaixo).

## 4. API → Postgres (last value)

Tabela `device_readings_latest`, chave composta (`device_id`, `sensor_type`), sobrescrita a cada leitura — ver [[Api (Quarkus)]].

## 5. API → ClickHouse (histórico)

Tabela append-only `readings_history`, particionada por data — ver [[Fase 7 - ClickHouse e Historico]].

## Decisões em aberto
- [ ] Epoch vs ISO-8601 entre as fronteiras — escolher um e documentar aqui.
- [ ] Versionamento do contrato (ex.: campo `schemaVersion`) — útil quando adicionarmos sensores novos.
- [ ] Unidades: normalizar sempre para SI (Celsius, %) no firmware ou no ingestion?

## Ver também
- [[Arquitetura Geral]]
- [[Esp32 - Firmware]], [[Ingestion Service (Go)]], [[Api (Quarkus)]]
