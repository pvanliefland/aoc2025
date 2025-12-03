"""Day three."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Find the total output joltage."""
    return (
        (total_output("day03_example.txt", 2), total_output("day03_example.txt", 12)),
        (total_output("day03.txt", 2), total_output("day03.txt", 12)),
    )


def total_output(file_path: str, max_batteries: int) -> int:
    """Find the output joltage for the battery banks (parts 1 & 2)."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    return sum(
        int("".join(best_batteries(line, max_batteries))) for line in data.splitlines()
    )


def best_batteries(line: str, remaining: int) -> list[str]:
    """Find the best batteries in line."""
    if remaining == 0:
        return []

    max_value, max_index = 0, 0
    for index, string_value in enumerate(line[: len(line) - remaining + 1]):
        value = int(string_value)
        if value > max_value:
            max_value, max_index = value, index

    return [str(max_value), *best_batteries(line[max_index + 1 :], remaining - 1)]
