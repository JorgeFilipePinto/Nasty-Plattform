---
tags: [deploy, extra]
---

# Domínio e DNS

Parte da rota A — ver [[Deploy em Producao - Visao Geral]]. Não necessário se fores só pela rota B ([[06 - Alternativa VPN WireGuard]]).

> Conceitos (o que é um domínio, DNS, registos, TTL, propagação): ver [[Dominio e DNS]] em `06 - Conceitos de Infraestrutura/`.

## Tasks
- [ ] Escolher e registar um domínio (ex.: `.dev`, `.com`, `.xyz` — qualquer um serve para aprendizagem).
- [ ] Escolher um DNS provider (pode ser o próprio registrar, ou separar — ex.: registar em qualquer sítio e usar Cloudflare DNS, que é grátis e tem proxy/CDN opcional).
- [ ] Apontar os nameservers do domínio para o DNS provider escolhido.
- [ ] Criar registos DNS depois de teres o IP do VPS (ver [[02 - VPS e Hardening]]):
  - `A dominio.com → <IP do VPS>`
  - `A api.dominio.com → <IP do VPS>`
  - `A dashboard.dominio.com → <IP do VPS>` (ou usar o domínio raiz para o dashboard e `api.` só para a API — decisão de gosto).
  - (Opcional) `A mqtt.dominio.com → <IP do VPS>`, se quiseres o broker acessível publicamente (ver nota de segurança em [[03 - NGINX Reverse Proxy]] — normalmente preferível deixar o MQTT só atrás da VPN, ver [[06 - Alternativa VPN WireGuard]]).

## Ver também
- [[02 - VPS e Hardening]]
- [[03 - NGINX Reverse Proxy]]
- [[Dominio e DNS]] (conceito)
