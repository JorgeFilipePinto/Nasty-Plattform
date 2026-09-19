---
tags: [deploy, extra]
---

# Deploy em Produção — Visão Geral

> ⚠️ **Não prioritário.** Esta secção só faz sentido depois de todas as fases do [[Roadmap]] estarem concluídas localmente (ESP32 → MQTT → Ingestion → Api → dashboard a funcionar via `docker compose`). É o último passo: tirar tudo de `localhost` e torná-lo acessível de fora. Não bloqueia nenhuma fase anterior.

## Objetivo
Pegar na stack completa (já a funcionar localmente) e expô-la para fora da rede local, por uma de duas rotas — **escolher uma para começar**, não é preciso fazer as duas:

| Rota | Quando escolher |
|---|---|
| **A. Domínio público + VPS + NGINX** — ver [[01 - Dominio e DNS]] → [[05 - Acesso via Dominio Publico]] | Queres que o dashboard/API sejam acessíveis por qualquer pessoa, com HTTPS normal, sem instalar nada no dispositivo cliente. |
| **B. VPN privada (WireGuard)** — ver [[06 - Alternativa VPN WireGuard]] | Só tu (e os teus dispositivos/ESP32) precisam de aceder; queres a menor superfície de ataque possível e não precisas de domínio nem certificados públicos. |

Nada impede de começar pela B (mais simples e barata) e mais tarde adicionar a A.

## Ordem sugerida (rota A — domínio público)
1. [[01 - Dominio e DNS]] — comprar domínio, configurar DNS.
2. [[02 - VPS e Hardening]] — provisionar a máquina, segurança básica.
3. [[03 - NGINX Reverse Proxy]] — entrypoint único, TLS, roteamento.
4. [[04 - Deploy da Aplicacao]] — levar a stack (`docker compose`) para o VPS.
5. [[05 - Acesso via Dominio Publico]] — validação fim-a-fim com o domínio real.

## Ordem sugerida (rota B — VPN)
1. [[02 - VPS e Hardening]] (ou um host doméstico, ex. Raspberry Pi) — só a máquina, sem domínio nem NGINX.
2. [[04 - Deploy da Aplicacao]] — a stack a correr nessa máquina.
3. [[06 - Alternativa VPN WireGuard]] — WireGuard a expor a stack só à rede privada.

## Pré-requisitos gerais
- Cartão de crédito/débito para registar domínio (rota A) e/ou alugar VPS (ambas as rotas, se não usares um host doméstico).
- Conta num registrar de domínios (ex.: Cloudflare, Namecheap) — só rota A.
- Conta num provedor de VPS (ex.: Hetzner, DigitalOcean, OVH).

## Ver também
- [[Arquitetura Geral]] — o que estamos a expor.
- [[Deployment (Docker Compose)]] — a base (`docker-compose.yaml`) que esta secção leva para produção.
- `06 - Conceitos de Infraestrutura/` — os "porquês" por trás de cada task desta secção (domínio/DNS, VPS, reverse proxy, TLS, VPN). As notas de tasks acima linkam para lá quando relevante.
