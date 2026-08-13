# AGENTS.md

## Repository status

Fresh scaffold — no buildable code yet. Only `README.md`, a generic C/C++/CMake `.gitignore`, and empty placeholder directories. Do not assume any tooling exists; verify before running build/test/lint commands.

## Layout

- `Api/` — backend, planned as a Spring Boot (Java) service
- `Esp32/` — firmware, planned as ESP-IDF (C/C++/CMake) project
- `Platform/` — frontend, planned as an Angular app
- `Deployment/Local/` — local deployment, currently an empty `docker-compose.yaml`
- `docs/` — developer docs (PT-BR): `docs/desenvolvimento.md` (workflow + per-component commands) and `docs/roadmap.md` (phases, tasks, release/tag convention). Read before starting work.

## Conventions

- ESP-IDF projects use CMake and produce build artifacts under `build/` (already git-ignored, along with other C/C++ artifacts). Keep `Esp32/` at the repo root free of generated files.
- Update `AGENTS.md` with real build, test, and lint commands for each component as they land; none exist yet.
