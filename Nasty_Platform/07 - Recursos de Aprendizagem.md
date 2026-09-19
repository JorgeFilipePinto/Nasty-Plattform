---
tags: [recursos, extra]
---

# Recursos de Aprendizagem

Página única com material de apoio externo (documentação oficial, tutoriais, vídeos, repositórios de exemplo) para cada parte do projeto. Cada secção abaixo começa com "**Ver no vault:**" a apontar para a(s) nota(s) correspondente(s) — é lá que estão as tasks e decisões deste projeto; aqui é só o material para aprender o conceito/tecnologia antes (ou durante) de as executar.

> Legenda: 📄 documentação/artigo · 🎥 vídeo · 💻 repositório de exemplo

---

## Firmware ESP32 (ESP-IDF)

**Ver no vault:** [[Esp32 - Firmware]] · [[Fase 1 - Nucleo Agnostico do Firmware]] · [[Fase 2 - Sensor e MQTT no Firmware]]

- 📄 [ESP-IDF Programming Guide — Get Started](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html) — instalação e primeiro projeto (`hello_world`), oficial da Espressif.
- 📄 [Getting Started with ESP-IDF: ESP32 Blink Project Guide](https://medium.com/engineering-iot/getting-started-with-esp-idf-building-your-first-blink-project-70adb2459f86) — passo a passo mais informal do primeiro projeto.
- 📄 [ESP-MQTT — ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/mqtt.html) — API oficial do cliente MQTT usado no firmware (Fase 2).
- 📄 [Over The Air Updates (OTA) — ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html) — API oficial (`esp_https_ota`, partições, rollback) — ver [[Esp32 - OTA (Atualizacoes Over-The-Air)]].
- 💻 [esp-idf/examples/system/ota — repositório oficial](https://github.com/espressif/esp-idf/blob/master/examples/system/ota/README.md) — exemplos `native_ota_example`, `simple_ota_example`, `advanced_https_ota`.
- 💻 [routevegetable/esp32-DHT](https://github.com/routevegetable/esp32-DHT) e [Andrey-m/DHT22-lib-for-esp-idf](https://github.com/Andrey-m/DHT22-lib-for-esp-idf) — drivers DHT11/DHT22 prontos para ESP-IDF, úteis para comparar com a implementação de `DHT_sensor.cpp`.
- 📄 [ESP32 - DHT22 | ESP32 Tutorial (esp32io.com)](https://esp32io.com/tutorials/esp32-dht22) — wiring e leitura do sensor.

## Interfaces e Abstração (C++)

**Ver no vault:** [[Interfaces e Abstracao]] · [[Principios de Design]]

- 🎥 [C++ Interfaces Explained: Abstract Classes & Polymorphism for Beginners](https://www.youtube.com/watch?v=xyevQt4w23w)
- 🎥 [C++ Tutorial: Abstract Classes and Interfaces](https://www.youtube.com/watch?v=FGToBKDO8Zc)
- 📄 [Interfaces in C++ (Abstract Classes) — TutorialsPoint](https://www.tutorialspoint.com/cplusplus/cpp_interfaces.htm) — referência rápida da sintaxe (`= 0`, classes puramente virtuais) usada em `ISensor.h`.

## MQTT e Mosquitto

**Ver no vault:** [[MQTT - Conceitos]] · [[Fase 3 - Broker MQTT e Ingestion Service]]

- 📄 [MQTT Essentials — HiveMQ](https://www.hivemq.com/mqtt/) — guia escrito de referência (tópicos, QoS, retained, LWT).
- 🎥 [MQTT Basics: What is MQTT and How Does it Work?](https://www.youtube.com/watch?v=z4r4hIZcp40)
- 🎥 [MQTT Tutorial 1 — Introduction to MQTT](https://www.youtube.com/watch?v=TSwgZn2FKUw)
- 📄 [eclipse-mosquitto — Docker Hub (imagem oficial)](https://hub.docker.com/_/eclipse-mosquitto)
- 📄 [Setting up the Mosquitto MQTT Broker using Docker Compose — Pi My Life Up](https://pimylifeup.com/mosquitto-mqtt-docker/) — guia passo a passo com `docker-compose.yml`.

## Ingestion Service (Go)

**Ver no vault:** [[Ingestion Service (Go)]] · [[Fase 3 - Broker MQTT e Ingestion Service]] · [[Fase 4 - API Quarkus]]

- 📄 [A Tour of Go (go.dev/tour)](https://go.dev/tour/) — introdução interativa oficial à linguagem.
- 📄 [Tutorial: Get started with Go (go.dev)](https://go.dev/doc/tutorial/getting-started) — módulos, `go run`, `go test`.
- 📄 [Go by Example](https://gobyexample.com/) — referência rápida por tópico (goroutines, structs, interfaces, etc.).
- 📄 [How to Use MQTT in Golang with Paho Client — EMQ](https://www.emqx.com/en/blog/how-to-use-mqtt-in-golang) — subscriber/publisher com `eclipse/paho.mqtt.golang`.
- 📄 [mattn/go-sqlite3 (driver cgo)](https://github.com/mattn/go-sqlite3) e [modernc.org/sqlite (driver puro Go)](https://pkg.go.dev/modernc.org/sqlite) — as duas opções de driver SQLite a decidir em [[Ingestion Service (Go)]].
- 📄 [Golang SQLite3 Tutorial — GoLinuxCloud](https://www.golinuxcloud.com/golang-sqlite3/) — exemplos práticos de `database/sql` com SQLite.

## Ports & Adapters (Arquitetura Hexagonal)

**Ver no vault:** [[Ports and Adapters (Arquitetura Hexagonal)]]

- 📄 [Hexagonal Architecture/Ports And Adapters: Clarifying Key Concepts Using Go](https://dev.to/buarki/hexagonal-architectureports-and-adapters-clarifying-key-concepts-using-go-14oo)
- 📄 [Hexagonal Architecture in Golang (Ports and Adapter Pattern)](https://medium.com/@sourav.ahmed5654/a-practical-guide-to-hexagonal-architecture-in-golang-0465f53eb2a5)
- 📄 [Building RESTful API with Hexagonal Architecture in Go](https://dev.to/bagashiz/building-restful-api-with-hexagonal-architecture-in-go-1mij) — exemplo completo de estrutura de projeto (`cmd`, `internal`, portas/adapters).

## Api (Quarkus)

**Ver no vault:** [[Api (Quarkus)]] · [[Fase 4 - API Quarkus]] · [[Fase 6 - Tempo Real (SSE-WebSocket)]]

- 📄 [Quarkus — Get Started (oficial)](https://quarkus.io/get-started/)
- 💻 [quarkusio/quarkus-quickstarts (repo oficial de exemplos)](https://github.com/quarkusio/quarkus-quickstarts)
- 📄 [Building a Full-Stack Todo App with Quarkus, Panache, and Qute](https://www.the-main-thread.com/p/quarkus-fullstack-todo-app-java-panache-qute) — REST + Panache + Postgres de ponta a ponta.
- 📄 [Using Flyway — Quarkus (guia oficial)](https://quarkus.io/guides/flyway/) — migrations versionadas (task da [[Fase 4 - API Quarkus]]).
- 💻 [auryn31/server-sent-event-quarkus](https://github.com/auryn31/server-sent-event-quarkus) — exemplo de SSE em Quarkus (Fase 6).
- 📄 [Testing your application — Quarkus (guia oficial)](https://quarkus.io/guides/getting-started-testing/) e [Development and Testing of Quarkus applications using Testcontainers](https://testcontainers.com/guides/development-and-testing-quarkus-application-using-testcontainers/).

## Bases de Dados: Postgres e ClickHouse

**Ver no vault:** [[Postgres vs ClickHouse]] · [[Fase 4 - API Quarkus]] · [[Fase 7 - ClickHouse e Historico]]

- 📄 [PostgreSQL — Tutorial oficial (Part I)](https://www.postgresql.org/docs/current/tutorial.html)
- 🎥 [PostgreSQL Tutorial for Beginners — Full Course (2026)](https://www.youtube.com/watch?v=u3Xyw6DXm_o)
- 📄 [ClickHouse Docs — Time-Series](https://clickhouse.com/docs/use-cases/time-series) — guia oficial para o caso de uso deste projeto (histórico de leituras).
- 📄 [ClickHouse Server in 1 minute with Docker](https://dev.to/titronium/clickhouse-server-in-1-minute-with-docker-4gf2) — arranque rápido local.
- 💻 [ClickHouse/postgres-clickhouse-stack](https://github.com/ClickHouse/postgres-clickhouse-stack/blob/main/docker-compose.yaml) — exemplo de `docker-compose` com Postgres + ClickHouse juntos.

## Platform (Dashboard Angular)

**Ver no vault:** [[Platform (Dashboard Angular)]] · [[Fase 5 - Dashboard Angular Polling]] · [[Fase 6 - Tempo Real (SSE-WebSocket)]]

- 📄 [Angular — Your first Angular app (tutorial oficial)](https://angular.dev/tutorials/first-app)
- 📄 [How to do polling with RxJs and Angular?](https://blog.angulartraining.com/how-to-do-polling-with-rxjs-and-angular-50d635574965) — `timer` + `switchMap`, a base da Fase 5.
- 📄 [Real-Time Communication in Angular: SSE vs WebSocket](https://aptuz.com/blog/a-dive-into-sse-and-web-sockets-in-angular/) — comparação direta, relevante para a decisão em [[Fase 6 - Tempo Real (SSE-WebSocket)]].

## Deploy em Produção — Infraestrutura

**Ver no vault:** [[Deploy em Producao - Visao Geral]] e as notas em `06 - Conceitos de Infraestrutura/`

- 📄 [Get Started — Let's Encrypt](https://letsencrypt.org/getting-started/) e [Certbot (oficial)](https://certbot.eff.org/) — ver [[TLS e Certificados (Lets Encrypt)]].
- 📄 [Setting up an Nginx Reverse Proxy with Certbot Under Docker](https://www.naturalborncoder.com/2024/10/setting-up-an-nginx-reverse-proxy-with-certbot-under-docker/) — ver [[Reverse Proxy e NGINX]] / [[03 - NGINX Reverse Proxy]].
- 🎥 [Ultimate Docker Compose Tutorial](https://www.youtube.com/watch?v=SXwC9fSwct8) — ver [[Deployment (Docker Compose)]] / [[04 - Deploy da Aplicacao]].
- 📄 [WireGuard — Quick Start (oficial)](https://www.wireguard.com/quickstart/) e [WireGuard VPN site-to-site — Ubuntu Server docs](https://ubuntu.com/server/docs/how-to/wireguard-vpn/site-to-site/) — ver [[VPN e WireGuard]].
- 🎥 [Easy WireGuard VPN Setup with Docker and WG-Easy](https://www.youtube.com/watch?v=3aRENOYwlcM) — ver [[06 - Alternativa VPN WireGuard]].
- 📄 [Setting up a WireGuard VPN using Docker — Pi My Life Up](https://pimylifeup.com/wireguard-docker/)

## Ver também
- [[00 - Home]] — mapa geral do vault.
- [[Roadmap]] — onde cada um destes recursos entra na ordem de trabalho.
