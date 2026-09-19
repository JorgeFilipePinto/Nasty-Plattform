# AGENTS.md

## Repository status

Fresh scaffold — no buildable code yet. Only `README.md`, a generic C/C++/CMake `.gitignore`, and empty placeholder directories. Do not assume any tooling exists; verify before running build/test/lint commands.

## Layout

- `Api/` — backend, planned as a Quarkus (Java) service; receives processed readings from `Ingestion/`, persists to Postgres (last value) and ClickHouse (history), serves the dashboard
- `Esp32/` — firmware, ESP-IDF (C/C++/CMake) project; agnostic core (Wi-Fi, scheduler, MQTT publish) + sensors behind the `ISensor` interface (already scaffolded under `Esp32/components/sensors/`)
- `Ingestion/` — planned Go service: subscribes MQTT, buffers readings in local SQLite, forwards to `Api/`
- `Platform/` — frontend, planned as an Angular app
- `Deployment/Local/` — local deployment, currently an empty `docker-compose.yaml` (will host Mosquitto, Postgres, ClickHouse, Prometheus)
- `docs/` — developer docs (PT-BR): `docs/desenvolvimento.md` (workflow + per-component commands) and `docs/roadmap.md` (points into the vault below)
- `Vault/` — Obsidian vault (PT-BR): the living architecture, roadmap and per-component task notes. Start at `Vault/00 - Home.md`. This is the source of truth for the current architecture (MQTT-first, multiple ESP32 devices, Ingestion service → Api → Postgres/ClickHouse) — read it before starting any task in this repo.

## Conventions

- ESP-IDF projects use CMake and produce build artifacts under `build/` (already git-ignored, along with other C/C++ artifacts). Keep `Esp32/` at the repo root free of generated files.
- Update `AGENTS.md` with real build, test, and lint commands for each component as they land; none exist yet.
