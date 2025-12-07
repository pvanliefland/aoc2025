"""Day seven."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Fix the teleporter."""
    return tachyon_split("day07_example.txt"), tachyon_split("day07.txt")


def tachyon_split(file_path: str) -> tuple[int, int]:
    """Do the thing with the tachyon beams."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    rows: list[list[str]] = [list(row) for row in data.splitlines()]
    beams = {(rows[0].index("S"), 0)}
    max_x = len(rows[0]) - 1
    split_count = 0
    timelines = 0

    for index, row in enumerate(rows[2:]):
        new_beams: set[tuple[int, int]] = set()
        same_beams = set()
        for beam in beams:
            if row[beam[0]] == "^":
                split_count += 1
                if beam[0] != 0:
                    new_beams.add((beam[0] - 1, beam[1] + 1))
                if beam[0] != max_x:
                    new_beams.add((beam[0] + 1, beam[1] + 1))
            else:
                same_beams.add((beam[0], beam[1] + 1))

        beams = new_beams | same_beams
        if index % 2 == 1:
            timelines += len(beams)

    return (split_count, timelines)
