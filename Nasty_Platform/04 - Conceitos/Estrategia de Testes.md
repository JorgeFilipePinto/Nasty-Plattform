---
tags: [conceito]
---

# Estratégia de Testes

## Princípio geral
Se um componente depende de [[Interfaces e Abstracao|interfaces]] (ver [[Principios de Design]]), consegue ser testado com implementações "fake"/mock das suas dependências, sem hardware, sem broker, sem BD real.

## Por componente
| Componente | O que testar | Como (sem dependências externas) |
|---|---|---|
| [[Esp32 - Firmware]] | Lógica do scheduler/wiring | `ISensor` fake que devolve valores fixos |
| [[Ingestion Service (Go)]] | Validação/normalização, lógica de retry | `Subscriber`/`Storage`/`Forwarder` fake (testes de tabela em Go) |
| [[Api (Quarkus)]] | Validação de entrada, service layer | `@QuarkusTest` com repositórios fake/in-memory; testes de integração com Testcontainers para Postgres/ClickHouse reais |
| [[Platform (Dashboard Angular)]] | Componentes e service | `HttpClientTestingModule`, testes de componente do Angular |

## Regra do projeto
Toda a task que adiciona lógica não-trivial (validação, retry, agregação) deve vir acompanhada de pelo menos um teste — reforça o objetivo de "skills de desenvolvimento de código" do projeto.

## Ver também
- [[Ports and Adapters (Arquitetura Hexagonal)]]
