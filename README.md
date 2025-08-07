
---
# Pricing Backend

Simple API for managing book records.

Some of the libraries used for implementation:
- FastAPI
- Asynchronous SQLAlchemy
- Alembic migrations


## Getting Started

Before starting, ensure Docker Compose is installed since this project is completely dockerized.

Copy `.env.example` file and rename it `.env`
```bash
cp .env.example .env
```

Start API service

```bash
docker compose up app
```
You should see logs like this, that means everything is up and running
``` bash
app  | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
app  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
app  | INFO:     Will watch for changes in these directories: ['/app']
app  | INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
app  | INFO:     Started reloader process [8] using StatReload
app  | INFO:     Started server process [10]
app  | INFO:     Waiting for application startup.
app  | INFO:     Application startup complete.
```

## Testing

Just in case, before starting tests, ensure that other services are down
```bash
docker compose down
```

```bash
docker compose up run_test_script
```
Since there's some time app service needs to start, this command will sleep approx. 15 seconds and then run test script.

### Note:
If you modify code, you'll need to rebuild docker images for `test` service.

```bash
docker compose build
```