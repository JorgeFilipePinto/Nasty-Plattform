---
tags: [deploy, extra]
---

# Acesso via Domínio Público

Passo final da rota A — ver [[Deploy em Producao - Visao Geral]]. Junta tudo: [[01 - Dominio e DNS]] + [[02 - VPS e Hardening]] + [[03 - NGINX Reverse Proxy]] + [[04 - Deploy da Aplicacao]].

## Fluxo fim-a-fim esperado
1. Browser pede `https://dashboard.dominio.com`.
2. DNS resolve o nome para o IP do VPS ([[01 - Dominio e DNS]]).
3. NGINX no VPS recebe o pedido na porta 443, termina TLS ([[03 - NGINX Reverse Proxy]]).
4. NGINX encaminha para o container do dashboard (estático) ou, para chamadas à API, para o container da `Api`.
5. Dashboard chama `https://api.dominio.com/...`, que segue o mesmo caminho até ao container da `Api`.
6. O ESP32, se publicar diretamente para o broker público, liga-se a `mqtt.dominio.com:8883` (TLS) — só se tiveres optado por expor o MQTT publicamente em [[03 - NGINX Reverse Proxy]]; caso contrário, o ESP32 fica na rota B ([[06 - Alternativa VPN WireGuard]]).

## Checklist de validação
- [ ] `https://dashboard.dominio.com` carrega com certificado válido (cadeado no browser).
- [ ] `https://api.dominio.com/readings/latest` responde.
- [ ] Uma leitura publicada por um ESP32 (ou pelo simulador) aparece no dashboard público em poucos segundos.
- [ ] Reiniciar o VPS não perde dados (volumes persistentes — ver [[04 - Deploy da Aplicacao]]).
- [ ] Portas internas (Postgres, ClickHouse, Mosquitto sem TLS) continuam inacessíveis de fora (`nmap`/`curl` de outra máquina para confirmar).

## Ver também
- [[Arquitetura Geral]]
