---
tags: [moc]
---

# Nasty-Plattform — Mapa de Aprendizagem

Vault Obsidian com a arquitetura, roadmap e tasks do projeto **Nasty-Plattform**: uma plataforma IoT de ponta a ponta (ESP32 → MQTT → serviço de ingestão → API → dashboard) usada como laboratório de **arquitetura de software** e **skills de desenvolvimento de código**.

> Para o guia de setup/comandos por componente, ver `docs/desenvolvimento.md` no repositório. Este vault é o mapa vivo de arquitetura, decisões e tasks.

## Por onde começar
- [[Arquitetura Geral]] — visão de ponta a ponta, diagrama, responsabilidades de cada peça.
- [[Roadmap]] — fases do projeto, cada uma com a sua nota e checklist.
- [[Principios de Design]] — o porquê da arquitetura agnóstica (interfaces, ports & adapters).
- [[07 - Recursos de Aprendizagem]] — documentação, tutoriais e vídeos externos, organizados por componente/fase.

## Componentes
- [[Esp32 - Firmware]]
- [[Esp32 - OTA (Atualizacoes Over-The-Air)]]
- [[Ingestion Service (Go)]]
- [[Api (Quarkus)]]
- [[Platform (Dashboard Angular)]]
- [[Deployment (Docker Compose)]]

## Conceitos (para consolidar skills)
- [[Interfaces e Abstracao]]
- [[Ports and Adapters (Arquitetura Hexagonal)]]
- [[Arquitetura em Camadas (Layered Architecture)]]
- [[Arquitetura de Componentes (Angular)]]
- [[MQTT - Conceitos]]
- [[SQLite como Buffer Local]]
- [[Postgres vs ClickHouse]]
- [[Estrategia de Testes]]

## Deploy em produção (extra, não prioritário)
Só relevante depois de todas as fases do [[Roadmap]] estarem feitas localmente — ver [[Deploy em Producao - Visao Geral]].

## Conceitos de Infraestrutura (extra, suporte ao deploy)
Base teórica para a secção de deploy — cada nota de task em `05 - Deploy em Producao/` linka para a nota correspondente aqui:
- [[Dominio e DNS]]
- [[VPS e Cloud]]
- [[Firewall e Hardening Basico]]
- [[Reverse Proxy e NGINX]]
- [[TLS e Certificados (Lets Encrypt)]]
- [[VPN e WireGuard]]

## Convenção deste vault
- Cada **Fase** do roadmap tem uma nota própria em `02 - Roadmap/`, com objetivo, tasks e definição de pronto.
- Cada **Componente** tem uma nota própria em `03 - Componentes/`, descrevendo responsabilidades, interfaces/contratos e tasks técnicas (não amarradas a uma fase só).
- Notas de **Conceitos** (`04 - Conceitos/`, arquitetura/software) e **Conceitos de Infraestrutura** (`06 - Conceitos de Infraestrutura/`, deploy/rede) existem para consolidar o "porquê" por trás das decisões, separado das tasks — úteis para revisão e para quem só quer estudar o conceito isolado.
- `05 - Deploy em Producao/` e `06 - Conceitos de Infraestrutura/` são **extra e não prioritários** — só entram em jogo no fim, para levar a stack para fora da rede local (domínio público ou VPN).
- Usa o grafo do Obsidian (`Ctrl/Cmd+G`) para navegar pelas ligações entre fases, componentes e conceitos.
