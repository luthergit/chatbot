#!/usr/bin/env bash
set -euo pipefail

uv sync
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload 