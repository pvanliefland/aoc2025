"""AOC 2025 main module."""

import argparse
from importlib import import_module

VALID_DAYS = range(1, 12)


def run() -> None:
    """Run main entrypoint."""
    parser = argparse.ArgumentParser(
        prog="AOC 2025",
        description="Just your usual AOC CLI.",
        epilog="Happy holidays 🎉",
    )

    parser.add_argument("day", type=int, help="The puzzle day (01, 02...)")

    args = parser.parse_args()
    if args.day not in VALID_DAYS:
        message = "Please specify a valid day (between 1 and 12)"
        raise ValueError(message)

    module = import_module(f"aoc2025.day{args.day:02}")
    ((example_part1, example_part2), (part1, part2)) = module.puzzle()

    print(f"Day {args.day:02} 🎄")
    print(f"Part 1: {part1} (example: {example_part1})")
    print(f"Part 2: {part2} (example: {example_part2})")
