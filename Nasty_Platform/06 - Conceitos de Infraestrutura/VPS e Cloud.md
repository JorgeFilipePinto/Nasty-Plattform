---
tags: [conceito, infraestrutura]
---

# VPS e Cloud

## O que é um VPS
Um **VPS** (Virtual Private Server) é uma máquina virtual isolada, com o seu próprio SO, IP público e recursos dedicados (vCPU, RAM, disco), alugada a um provedor (Hetzner, DigitalOcean, OVH, ...). Ao contrário de hosting partilhado, tens acesso root/sudo total — podes instalar Docker, correr o que quiseres.

## Porque um VPS e não outra coisa
| Opção | Quando faz sentido |
|---|---|
| **VPS** | Controlo total, previsível em custo, suficiente para uma stack pequena/média — a escolha deste projeto. |
| Hosting partilhado (PHP/cPanel, etc.) | Sites simples sem controlo sobre containers/processos — não serve para `docker compose`. |
| Serverless / PaaS (ex. Fly.io, Render) | Menos operação manual, mas menos controlo e por vezes mais caro à escala, e mais difícil de correr uma stack multi-serviço com estado (Postgres, ClickHouse) tudo junto. |
| Bare metal | Só compensa a partir de volumes/performance que este projeto não precisa. |

## Dimensionamento (heurística, não é preciso ser exato)
- **vCPU**: 2 é suficiente para começar (Mosquitto, Api, Ingestion, Postgres e ClickHouse não são individualmente pesados a este volume de dados).
- **RAM**: 4 GB dá alguma margem — ClickHouse é o serviço mais sensível a RAM se o histórico crescer bastante.
- **Disco**: SSD, tamanho depende de quanto histórico queres guardar (ClickHouse comprime bem, mas cresce com o tempo).

## Acesso e primeira configuração
- Acesso inicial normalmente por SSH com password ou chave fornecida pelo provedor — o primeiro passo é sempre trocar para autenticação por chave pública e desativar password (ver [[Firewall e Hardening Basico]]).
- O IP público atribuído ao VPS é o que entra nos registos DNS (ver [[Dominio e DNS]]).

## Neste projeto
Ver a aplicação prática em [[02 - VPS e Hardening]].

## Ver também
- [[Firewall e Hardening Basico]]
- [[Reverse Proxy e NGINX]]
- [[Deploy em Producao - Visao Geral]]
