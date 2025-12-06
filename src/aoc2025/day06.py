"""Day six."""

import re
from functools import reduce
from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Do the cephalopod math homework."""
    return (math_homework("day06_example.txt"), math_homework("day06.txt"))


def math_homework(file_path: str) -> tuple[int, int]:
    """Do the homework as a human, then as a cephalopod."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    rows = data.splitlines()
    numbers = [[int(n) for n in r.split()] for r in rows[:-1]]
    raw_instructions = re.findall(r"(\+|\*)(\s+)", rows[-1] + " ")
    instructions_and_digits = [(raw[0], len(raw[1])) for raw in raw_instructions]

    operations_part_1 = [
        (col[:-1], col[-1][0])
        for col in list(zip(*numbers, instructions_and_digits, strict=True))
    ]

    operations_part_2 = []
    start = 0
    for instruction, digits in instructions_and_digits:
        raw_numbers = [row[start : start + digits] for row in rows[:-1]]
        cephalopod_numbers = [int("".join(n)) for n in zip(*raw_numbers, strict=True)]
        operations_part_2.append((cephalopod_numbers, instruction))
        start += digits + 1

    return compute(operations_part_1), compute(operations_part_2)


def compute(operations: list[tuple[tuple[int], str]]) -> int:
    """Do the math."""
    return sum(
        sum(n) if i == "+" else reduce(lambda x, y: x * y, n) for n, i in operations
    )
