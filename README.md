# Scalable Document Processing and Analysis Pipeline on Kubernetes

## Project Overview

This project will design and implement a scalable document processing and analysis pipeline deployed on Kubernetes.

Users will submit text documents through an application programming interface (API). Documents will move through separate services for preprocessing, analysis, and storage. The analysis service will extract characteristics such as word count, sentence count, frequently occurring words, and basic sentiment.

The project will demonstrate cloud-native concepts including:

- Multi-pod application architecture
- Multi-container pods using a sidecar container
- Kubernetes service discovery
- Horizontal scaling
- Self-healing
- Persistent storage
- Health monitoring
- Container resource management

## Architecture

The proposed pipeline consists of four primary application components:

1. API Gateway
2. Document Preprocessing Service
3. Document Analysis Service
4. Storage Service

The API Gateway will serve as the application's external entry point, while the remaining components will communicate internally through Kubernetes Services.

## Documentation

The technical report for Project Deliverable 1 is included in this repository.

## Milestone 1: Local Development Setup (macOS Apple Silicon)

This milestone sets up a minimal FastAPI starter app with tests.

### Prerequisites

- macOS (Apple Silicon / M-chip)
- Python 3.11+
- Git

Check versions:

```bash
python3 --version
git --version
```

### Clone the repository

```bash
git clone https://github.com/tbellegue/kubernetes-document-pipeline.git
cd kubernetes-document-pipeline
```

### Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should now see `(.venv)` in your terminal prompt.

### Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run the app

```bash
uvicorn app.main:app --reload
```

App endpoints:

- Root: http://127.0.0.1:8000/
- Health: http://127.0.0.1:8000/health
- Swagger docs: http://127.0.0.1:8000/docs

Stop the server with `Ctrl + C`.

### Run tests

```bash
pytest -q
```

Expected output should include:

- `2 passed`

### Notes

- `pytest.ini` is included so tests can import the `app` package cleanly.
- A warning from `TestClient`/`httpx` may appear; this does not block Milestone 1 functionality.
