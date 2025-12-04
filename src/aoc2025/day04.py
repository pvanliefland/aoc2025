"""Day four."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Find how many rolls of paper can be accessed by forklifts."""
    return (
        (rolls("day04_example.txt"), rolls("day04_example.txt", recursive=True)),
        (rolls("day04.txt"), rolls("day04.txt", recursive=True)),
    )


def rolls(file_path: str, *, recursive: bool = False) -> int:
    """Find the accessible rolls of paper for map in file_path."""
    with Path(f"inputs/{file_path}").open() as input_file:
        return rolls_in_map(
            {
                (x, y): char
                for y, row in enumerate(input_file.read().splitlines())
                for x, char in enumerate(row)
            },
            recursive=recursive,
        )


def rolls_in_map(
    roll_map: dict[tuple[int, int], str], *, recursive: bool = False
) -> int:
    """Find the accessible rolls of paper for map in file_path."""
    accessible_rolls = 0
    for pos, char in roll_map.items():
        if char != "@":
            continue

        adjacent_rolls = 0
        for move in [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]:
            if roll_map.get((pos[0] + move[0], pos[1] + move[1])) == "@":
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            accessible_rolls += 1
            if recursive:
                roll_map[pos] = "."

    if recursive and accessible_rolls > 0:
        return accessible_rolls + rolls_in_map(roll_map, recursive=True)

    return accessible_rolls
