#!/usr/bin/env bash
set -euo pipefail

uv sync
uv run uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload 