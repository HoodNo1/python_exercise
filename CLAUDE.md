# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

Monorepo of Python exercises, each in a subdirectory (e.g., `project1/`). Each sub-project is self-contained with its own `pyproject.toml`.

## Package Manager

This repo uses **uv** (https://docs.astral.sh/uv/) for Python package management.

- `uv sync` — Install dependencies from `uv.lock`
- `uv add <package>` — Add a new dependency
- `uv remove <package>` — Remove a dependency
- `uv run python <script>` — Run a script with the project's environment
- `uv run <command>` — Run any command in the project's virtual environment

## Running a Project

```bash
cd project1
uv run python main.py
```

## Python Version

Requires Python >=3.14 (configured per-project in `pyproject.toml` and `.python-version`).
