# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Structure

Monorepo of Python exercise projects, each in a subdirectory (e.g., `project1/`). Each sub-project is self-contained with its own `pyproject.toml`.

## Package Manager

This repo uses **uv** (https://docs.astral.sh/uv/) for Python package management.

- `uv sync` — Install dependencies from `uv.lock`
- `uv add <package>` — Add a new dependency
- `uv remove <package>` — Remove a dependency
- `uv run python <script>` — Run a script with the project's environment
- `uv run <command>` — Run any command in the project's virtual environment

## Python Version

Requires Python >=3.14 (configured per-project in `pyproject.toml` and `.python-version`).

## Running a Practice File

```bash
cd project1
uv run python practice_01_datatypes_strings.py
```

## Exercise File Conventions

### Naming

Practice files follow the pattern `practice_XX_topic.py`, where `XX` is a zero-padded sequence number. Each file covers 2 grammar/syntax topics with ~30 exercises per file.

### File Structure

Each practice file contains:
- Module docstring describing the two topics covered
- Exercises grouped by topic with numbered subsections (e.g., `# 练习 1.1`, `# 练习 2.1`)
- Description comments explaining what to do
- `...` placeholders for code to be filled in by learners
- Commented-out `print()` and `assert` statements for verification
- A final print-and-assert block to validate the exercise

### Exercise Format

```python
# ---------------------------------------------------------------------------
# 练习 N.M —— Title
# Description of what to implement.
# ---------------------------------------------------------------------------

# Code with ... placeholders
result = ...

# Check
# print(f"output: {result}")
# assert result == expected_value
# print("练习 N.M 通过！")
```

### Creating a New Practice File

1. Copy the numbering pattern: `practice_XX_topic.py`
2. Start with a module docstring listing both topics
3. Split into two topic sections with `====` separators
4. Number exercises `1.1`..`1.N` for topic 1 and `2.1`..`2.N` for topic 2
5. Include realistic TODO `...` placeholders for learners to fill
6. Add commented-out assertions so learners can verify by uncommenting
7. End with a summary comment counting total exercises

### Rules for Exercise Comments

- **Never** put answers, results, or explanations in comments — let learners discover them
- Use questions (`# 思考：为什么？`) instead of statements (`# 原因是...`)
- Keep exercise descriptions neutral: describe *what to do*, not *what result to expect*
