---
tags: [conceito]
---

# Interfaces e Abstração

## Ideia central
Uma interface define **o que** um componente faz, não **como**. Quem depende da interface (ex.: o loop principal do firmware, ou o `Service` da API) não precisa de saber qual implementação concreta está por trás — pode até nem existir ainda.

## No firmware
```cpp
class ISensor {
public:
    virtual void init(int pin, int updateInterval = 60) = 0;
    virtual bool start() = 0;
    virtual bool read(SensorData& data) = 0;
    virtual ~ISensor() = default;
};
```
O loop principal (ver [[Esp32 - Firmware]]) só conhece `ISensor`. Adicionar um sensor novo (`LightSensor`, `SoilMoistureSensor`, ...) nunca implica tocar no loop — só criar a classe nova e fazer o wiring em `main.c`.

## Sinal de que a interface está bem desenhada
- O código que **usa** a interface não importa nenhum header/classe concreta.
- É possível criar uma implementação "fake" (para testes) sem esforço.
- Adicionar uma nova implementação não obriga a alterar as existentes (Open/Closed Principle).

## Onde mais se aplica neste projeto
- `Subscriber` / `Storage` / `Forwarder` no [[Ingestion Service (Go)]].
- `Repository` (Postgres/ClickHouse) na [[Api (Quarkus)]].

## Ver também
- [[Ports and Adapters (Arquitetura Hexagonal)]] — a mesma ideia, formalizada como padrão arquitetural.
- [[Principios de Design]]
