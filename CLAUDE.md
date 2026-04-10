# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A personal knowledge base of cheat sheets and reference documentation for various technologies. Content is primarily Markdown files organized by domain, with some runnable code examples (Python notebooks and scripts).

## Environment Setup

This project uses `uv` for Python dependency management (Python >=3.13 required):

```bash
uv sync          # install dependencies
uv run jupyter notebook   # launch notebooks
```

## Repository Structure

Content is organized into top-level domain directories:

- `agents/` — AI agent tools (Claude Code CLI, etc.)
- `cloud/` — Cloud platform docs (GCP: Vertex AI, GKE, IAM, Cloud Build, etc.)
- `computer_vision/` — OpenCV, blur detection
- `data/` — Sample datasets (CSV/TSV) used by notebooks and examples
- `data_engineering/` — dbt, Apache Beam/Dataflow, PySpark
- `data_management/` — SQL, Neo4j, Elasticsearch
- `data_science/` — EDA, preprocessing, metrics, cross-validation, XGBoost
- `data_validation/` — Pydantic
- `frontend/javascript/` — React, TypeScript, Next.js
- `git/` — GitHub Actions
- `infrastructure/` — Docker, Kubernetes, Drone CI
- `machine_learning/` — TensorFlow, PyTorch, LightGBM, NLP, LLMs, Kubeflow, Metaflow
- `MLOps/` — MLflow, BentoML, Neptune (with runnable examples under `examples/`)
- `notebooks/` — Standalone Jupyter notebooks (e.g., seaborn)
- `project_sample/` — Sample Python project structure showing `general_utils`, `logging_module`, `tests`, and `configuration` layout
- `python/` — Python library cheat sheets (pandas, matplotlib, poetry, uv, pre-commit, etc.)
- `rest_api/` — FastAPI
- `shell_scripting/` — Shell scripting reference
- `statistics/` — SciPy, statistics theory

## Content Conventions

- All cheat sheets are Markdown (`.md`) files — prefer editing existing files over creating new ones.
- MLOps `examples/` subdirectories contain runnable Python/notebook code alongside their `docs/` reference files.
- `project_sample/` demonstrates the preferred Python project layout (modules with `__init__.py`, `tests/` with fixtures).
- The `justfile/justfile_example_1` directory contains Just task runner examples.
