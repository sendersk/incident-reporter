# Incident Reporter

> REST API Incident Reporting Tool, designed to automate incident collection, storage, and report generation.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-purple)
![Ruff](https://img.shields.io/badge/linter-Ruff-red)
![MyPy](https://img.shields.io/badge/type%20checking-MyPy-blue)
![Pytest](https://img.shields.io/badge/tests-Pytest-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)

---

# Overview

Incident Reporter is a Python application that retrieves incident data from a REST API, stores it locally in JSON format, and generates human-readable Markdown and HTML reports.

The project demonstrates practical backend and DevOps skills, including:

- REST API integration
- JSON processing
- YAML configuration
- file operations
- report generation
- scheduling jobs
- Docker containerization
- clean project architecture
- automated testing

---

# Features

- Fetch incidents from REST API
- YAML configuration
- Pydantic data validation
- JSON persistence
- Markdown report generation
- HTML report generation (Jinja2)
- Scheduler for automatic execution (APScheduler)
- Docker support
- Docker Compose support
- Unit tests with Pytest
- Static analysis with Ruff
- Type checking with MyPy

---

# Project Structure

```text
incident-reporter/
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── compose.yaml
├── pyproject.toml
├── README.md
├── uv.lock
│
├── config/
│   └── config.yaml
│
├── data/
│
├── reports/
│
├── templates/
│   └── report.html.j2
│
├── tests/
│   ├── test_api.py
│   ├── test_html_report.py
│   ├── test_reporter.py
│   └── test_storage.py
│
└── src/
    └── incident_reporter/
        ├── __init__.py
        ├── api.py
        ├── config.py
        ├── main.py
        ├── models.py
        ├── pipeline.py
        ├── reporter.py
        ├── scheduler.py
        └── storage.py
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.13 |
| Package Manager | uv |
| HTTP Client | httpx |
| Configuration | YAML |
| Validation | Pydantic |
| HTML Templates | Jinja2 |
| Scheduler | APScheduler |
| Testing | Pytest |
| Linting | Ruff |
| Type Checking | MyPy |
| Containerization | Docker |

---

# Installation

Clone the repository

```bash
git clone https://github.com/sendersk/incident-reporter.git

cd incident-reporter
```

Install dependencies

```bash
uv sync
```

---

# Configuration

Edit

```text
config/config.yaml
```

Example

```yaml
api:
  url: "https://jsonplaceholder.typicode.com/posts"

storage:
  file: "data/incidents.json"

reports:
  markdown: "reports/incident_report.md"
  html: "reports/incident_report.html"
```

---

# Running the application

Execute once

```bash
uv run python -m incident_reporter.main
```

---

# Scheduler Mode

Generate reports automatically every minute.

```bash
uv run python -m incident_reporter.main --schedule
```

---

# Generated Files

JSON storage

```text
data/incidents.json
```

Markdown report

```text
reports/incident_report.md
```

HTML report

```text
reports/incident_report.html
```

---

# Running Tests

```bash
uv run pytest
```

---

# Ruff

```bash
uv run ruff check .
```

Fix automatically

```bash
uv run ruff check . --fix
```

---

# MyPy

```bash
uv run mypy src
```

---

# Docker

Build image

```bash
docker build -t incident-reporter .
```

Run application

```bash
docker run --rm incident-reporter
```

---

# Docker Compose

Build and start

```bash
docker compose up --build
```

Run in background

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# Application Workflow

```text
REST API
    │
    ▼
API Client
    │
    ▼
Pydantic Models
    │
    ▼
JSON Storage
    │
    ├────────────► Markdown Report
    │
    └────────────► HTML Report
```

Scheduler mode

```text
Scheduler
     │
     ▼
Pipeline
     │
     ▼
REST API
     │
     ▼
Storage
     │
     ▼
Reports
```

---

# Example Output

```text
=== Incident Reporter ===

Fetched incidents : 100

JSON output       : data/incidents.json

Markdown report   : reports/incident_report.md

HTML report       : reports/incident_report.html

[PIPELINE] Finished successfully
```

---

# Future Improvements

- SQLite support
- PostgreSQL support
- Email notifications
- Slack integration
- Microsoft Teams integration
- PDF report generation
- Logging
- CLI interface (Typer)
- GitHub Actions CI/CD
- Kubernetes deployment

---

# Development

This project follows modern Python development practices:

- modular architecture
- clean code
- SOLID principles
- type hints
- static analysis
- automated testing
- containerization
- reproducible environments

---

# Author

Created by Przemysław Senderski
