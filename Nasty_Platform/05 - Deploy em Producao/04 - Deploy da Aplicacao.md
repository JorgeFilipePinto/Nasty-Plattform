---
tags: [deploy, extra]
---

# Deploy da Aplicação

Comum às duas rotas — ver [[Deploy em Producao - Visao Geral]]. É aqui que a stack que já corre localmente via `Deployment/Local/docker-compose.yaml` passa a correr no VPS (ou host escolhido).

## Tasks
- [ ] Criar um `docker-compose` de produção (ex.: `Deployment/Prod/docker-compose.yaml`), derivado do local mas com:
  - Volumes persistentes com bind mounts/volumes nomeados (Postgres, ClickHouse) para não perder dados entre restarts.
  - `restart: unless-stopped` em todos os serviços.
  - Variáveis sensíveis (passwords, tokens) via ficheiro `.env` **não commitado** (já coberto pelo `.gitignore` do repo).
  - Sem portas de serviços internos publicadas para o host (só o NGINX/WireGuard tocam o exterior — ver [[02 - VPS e Hardening]]).
- [ ] Build das imagens:
  - `Api/` — imagem Quarkus (JVM ou nativa via GraalVM, a decidir; nativa arranca mais depressa e usa menos RAM, mas o build é mais lento/exigente).
  - `Ingestion/` — binário Go compilado estaticamente, imagem mínima (`FROM scratch` ou `alpine`).
  - `Platform/` — build de produção do Angular (`ng build`) servido como estático (via NGINX, dentro ou fora do container).
- [ ] Escolher o mecanismo de deploy:
  - Simples: `git pull` + `docker compose up -d --build` manual no VPS.
  - Automatizado: pipeline CI/CD (ex. GitHub Actions) a fazer build, push das imagens para um registry, e um passo de deploy (SSH + `docker compose pull && up -d`, ou um webhook).
- [ ] Migrations (Flyway) a correrem automaticamente no arranque da Api, ou como um passo explícito do deploy.

## Notas
- Esta nota assume que as fases 0–9 do [[Roadmap]] já estão feitas — não há nada de arquitetura nova aqui, só "a mesma stack, noutra máquina, com mais cuidado operacional".
- Testar sempre primeiro com `docker compose config` (valida o ficheiro) antes de `up -d` em produção.

## Ver também
- [[Deployment (Docker Compose)]]
- [[05 - Acesso via Dominio Publico]]
- [[06 - Alternativa VPN WireGuard]]
