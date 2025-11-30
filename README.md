# AOC 2025 

My goals for this year's [Advent of Code](https://adventofcode.com/2025):

- Back to Python, after a few Rust years
- Vanilla Python, no dependencies
- Try out the latest features from Python 3.10+
- Modern tooling (`uv`, `ty` and `prek`)
- Zero AI - no code generation, no chat assistance

## Running the puzzles

Make sure you have a recent install of [`uv`](https://docs.astral.sh/uv/).

This project has a small CLI that you can use to run the puzzles:

```shell
uv run aoc2025 01
```

## Code quality

This project uses [`ruff`](https://docs.astral.sh/ruff) for linting, and [`ty`](https://docs.astral.sh/ty/)
for type-checking.

Pre-commit hooks are managed by [`prek`](https://prek.j178.dev/).

The easiest way to run code quality check is to use `prek`:

```shell
prek run --all-files
```
