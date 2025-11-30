# AOC 2025

## Running the puzzles

Make sure you have a recent install of [uv](https://docs.astral.sh/uv/).

This project has a small CLI that you can use to run the puzzles:

```bash
uv run aoc2025 01
```

## Code quality

This project uses [ruff](https://docs.astral.sh/ruff) for linting, and [ty](https://docs.astral.sh/ty/)
for type-checking.

Pre-commit hooks are managed by [prek](https://prek.j178.dev/).

The easiest way to run code quality check is to use `prek`:

```shell
prek run --all-files
```
