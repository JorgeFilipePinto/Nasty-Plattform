---
tags: [arquitetura, conceito]
---

# Princípios de Design

O objetivo declarado do projeto é "desenvolvimento arquitetural e de skills de desenvolvimento de código" — por isso a arquitetura é desenhada deliberadamente para treinar boas práticas, não só para "funcionar".

## 1. Agnosticismo por interface
> "Todas as classes têm de ser agnósticas; apenas a parte específica do sensor é individual."

Na prática:
- O firmware tem um núcleo **agnóstico** (Wi-Fi, MQTT, scheduler, montagem de payload) que não sabe nada sobre sensores concretos — só conhece a interface `ISensor`.
- Cada sensor concreto (`TempSensor`, e futuros `LightSensor`, `SoilMoistureSensor`, ...) implementa `ISensor` e é a **única** parte que muda por dispositivo.
- O mesmo padrão repete-se no `Ingestion Service` (subscriber/storage/forwarder como interfaces trocáveis) e na `Api` (repositórios Postgres/ClickHouse por trás de uma interface de serviço).

Ver [[Interfaces e Abstracao]] para o conceito genérico e [[Ports and Adapters (Arquitetura Hexagonal)]] para o padrão arquitetural que formaliza isto no backend.

## 2. Um contrato de dados explícito
As fronteiras entre componentes (ESP32→MQTT, Ingestion→API, API→BDs) são definidas em [[Contrato de Dados]] antes de existir código. Isto permite implementar cada componente de forma independente e até em paralelo.

## 3. Buffer local antes de rede
O `Ingestion Service` grava sempre primeiro em [[SQLite como Buffer Local]] antes de tentar encaminhar para a API — se a API estiver em baixo, os dados não se perdem. Ver [[Fase 3 - Broker MQTT e Ingestion Service]].

## 4. Cada fase é releasável
Ver [[Roadmap]] — cada fase entrega algo demonstrável de ponta a ponta (mesmo que mínimo), em vez de construir todas as camadas em paralelo até ao fim.

## 5. Testabilidade
Cada componente com lógica não-trivial (processamento no ingestion, service layer na API) deve ser testável sem depender de hardware real ou serviços externos — ver [[Estrategia de Testes]].

## Ver também
- [[Arquitetura Geral]]
