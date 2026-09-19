---
tags: [deploy, extra]
---

# NGINX — Reverse Proxy

Parte da rota A — ver [[Deploy em Producao - Visao Geral]]. Sim, usamos NGINX: é o entrypoint público único do VPS, faz terminação TLS e encaminha cada subdomínio/path para o container interno certo.

> Conceitos (o que é um reverse proxy, porquê, HTTP vs TCP puro, TLS/Let's Encrypt): ver [[Reverse Proxy e NGINX]] e [[TLS e Certificados (Lets Encrypt)]] em `06 - Conceitos de Infraestrutura/`.

## Roteamento previsto neste projeto
- `dashboard.dominio.com` → container do `Platform` (build estático).
- `api.dominio.com` → container da `Api` (Quarkus).

## Tasks
- [ ] Instalar `certbot` (ou usar o container `nginx-proxy` + `acme-companion` para automatizar tudo via Docker — mais prático quando tudo já corre em `docker compose`).
- [ ] Server block para `dashboard.dominio.com` → proxy para o container do dashboard.
- [ ] Server block para `api.dominio.com` → proxy para o container da Api, com os headers de upgrade necessários se/quando existir WebSocket/SSE (ver [[Fase 6 - Tempo Real (SSE-WebSocket)]]):
  ```nginx
  location / {
      proxy_pass http://api:8080;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
      proxy_http_version 1.1;
  }
  ```
- [ ] Emitir/renovar certificados (`certbot --nginx` ou automático via `acme-companion`); confirmar renovação automática (cron/systemd timer).
- [ ] (Só se decidires expor MQTT publicamente, em vez de o deixar atrás da VPN) módulo `stream` do NGINX para proxy TCP puro na porta `8883` (MQTT não é HTTP — o `location`/`proxy_pass` normal não serve; é preciso o bloco `stream {}` no `nginx.conf` a nível de servidor, não de `server {}` HTTP).

## Decisões em aberto
- [ ] Expor o broker MQTT publicamente (via `stream` do NGINX + TLS) vs deixá-lo só acessível através da VPN ([[06 - Alternativa VPN WireGuard]]) — a segunda opção é mais segura e é a recomendação por omissão deste projeto.
- [ ] Servir o build do Angular diretamente do NGINX do host (ficheiros estáticos) vs num container `nginx` próprio dedicado ao `Platform/`.

## Ver também
- [[04 - Deploy da Aplicacao]]
- [[05 - Acesso via Dominio Publico]]
- [[Reverse Proxy e NGINX]], [[TLS e Certificados (Lets Encrypt)]] (conceitos)
