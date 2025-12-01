"""Day one."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Compute the password for the North pole base."""
    return compute_password("day01_example.txt"), compute_password("day01.txt")


def compute_password(file_path: str) -> tuple[int, int]:
    """Compute password (part 1 and part 2)."""
    with Path(f"inputs/{file_path}").open() as example_input_file:
        data = example_input_file.read()
    position, password1, password2 = 50, 0, 0

    for line in data.splitlines():
        if line[0] == "L":
            distance, rotation = position, -int(line[1:])
        else:
            distance, rotation = (100 - position), int(line[1:])

        if abs(rotation) % 100 == distance:
            password1 += 1
        if abs(rotation) >= distance:
            password2 += (0 if distance == 0 else 1) + int(
                (abs(rotation) - distance) / 100
            )
        position = (position + rotation) % 100

    return password1, password2
