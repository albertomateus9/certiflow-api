# CertiFlow API

Certificate generation and validation architecture for educational programs, with cryptographic integrity and asynchronous processing in mind.

## Overview

CertiFlow API is an educational backend template for generating, signing, and validating school or training certificates at scale. It uses Clean Architecture to keep certificate rules independent from HTTP controllers, PDF rendering, queues, and storage choices.

## Problem

Manual certificate workflows are slow, hard to audit, and vulnerable to fraud. A professional certificate service needs deterministic validation, batch processing, and a clear separation between business rules and infrastructure.

## Core Ideas

- Generate a SHA-256 integrity hash from student and event data.
- Encode validation data into a QR Code or public verification endpoint.
- Process large certificate batches asynchronously through workers.
- Keep rendering and queue systems replaceable.

## Architecture

- `domain/`: student, event, and certificate entities.
- `application/`: generation and validation use cases.
- `interface_adapters/`: future FastAPI controllers and DTOs.
- `infrastructure/`: future PDF rendering, queues, templates, and storage.

## Stack

- Python 3.10+
- FastAPI and Uvicorn
- WeasyPrint and Jinja2 for PDF rendering
- QRCode generation
- Celery for asynchronous workloads

## Getting Started

```bash
git clone https://github.com/albertomateus9/certiflow-api.git
cd certiflow-api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On Linux or macOS, activate the environment with:

```bash
source .venv/bin/activate
```

## Development Direction

- Add CSV parsing for approved students.
- Implement Celery tasks for PDF generation.
- Expose certificate validation through FastAPI.
- Add persistence for issued certificates and verification status.
- Add tests for hash generation and validation use cases.

## Professional Context

This project connects educational technology, public-sector training workflows, software architecture, and security-minded documentation.

## License

MIT. See [LICENSE](LICENSE).
