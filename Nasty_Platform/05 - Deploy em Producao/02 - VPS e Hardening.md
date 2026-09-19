---
tags: [deploy, extra]
---

# VPS e Hardening

Base de qualquer uma das duas rotas — ver [[Deploy em Producao - Visao Geral]]. Se optares por não pagar um VPS, um host doméstico (ex. Raspberry Pi, ou o próprio computador sempre ligado) pode substituir isto para a rota B (VPN).

> Conceitos (o que é um VPS, dimensionamento, firewall, SSH hardening): ver [[VPS e Cloud]] e [[Firewall e Hardening Basico]] em `06 - Conceitos de Infraestrutura/`.

## Tasks — setup inicial
- [ ] Escolher o provedor (Hetzner, DigitalOcean, OVH, Scaleway, ...) e criar a VPS (Ubuntu/Debian LTS).
- [ ] Criar um utilizador não-root com `sudo`.
- [ ] Configurar acesso SSH por chave pública; desativar autenticação por password.
- [ ] Firewall (`ufw`): permitir só `22` (SSH), `80`/`443` (HTTP/HTTPS, rota A), e/ou a porta UDP do WireGuard (rota B). Tudo o resto fechado por omissão.
- [ ] `fail2ban` + atualizações automáticas de segurança.
- [ ] Instalar Docker + Docker Compose plugin.
- [ ] Instalar NGINX (rota A) — ver [[03 - NGINX Reverse Proxy]].

## Notas
- Guardar o IP público do VPS — é o que vai para os registos DNS ([[01 - Dominio e DNS]]).
- Nunca deixar as portas dos serviços internos (Postgres `5432`, ClickHouse `8123`/`9000`, Mosquitto `1883`) expostas diretamente à internet — só o NGINX (rota A) ou a interface da VPN (rota B) devem estar acessíveis de fora; os restantes serviços falam entre si só na rede interna do `docker compose`.

## Ver também
- [[04 - Deploy da Aplicacao]]
- [[06 - Alternativa VPN WireGuard]]
- [[VPS e Cloud]], [[Firewall e Hardening Basico]] (conceitos)
