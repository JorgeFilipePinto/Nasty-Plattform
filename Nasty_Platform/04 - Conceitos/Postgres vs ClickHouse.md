---
tags: [conceito]
---

# Postgres vs ClickHouse

## Porque duas bases de dados diferentes?
São otimizadas para padrões de acesso opostos:

| | Postgres | ClickHouse |
|---|---|---|
| Tipo | OLTP (transacional, relacional) | OLAP (analítico, colunar) |
| Uso neste projeto | *Last value* por device/sensor — leitura pontual, escrita com upsert | Histórico completo — escrita append-only em massa, leitura agregada (médias, séries temporais) |
| Padrão de query | "Dá-me o valor atual do device X" | "Dá-me a média por hora do sensor Y nas últimas 24h" |
| Escrita | Linha a linha, com update | Em lote (batch), nunca update |

Usar só uma das duas para tudo seria pior nos dois padrões de acesso — daí a separação na [[Api (Quarkus)]].

## Neste projeto
- Postgres: tabela `device_readings_latest`, upsert a cada leitura (ver [[Contrato de Dados]] §4).
- ClickHouse: tabela `readings_history`, append-only, introduzida na [[Fase 7 - ClickHouse e Historico]] (ver [[Contrato de Dados]] §5).

## Ver também
- [[Api (Quarkus)]]
