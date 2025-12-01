"""Day one."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Compute the password for the North pole base."""
    return compute_password("day01_example.txt"), compute_password("day01.txt")


def compute_password(file_path: str) -> tuple[int, int]:
    """Compute password (part 1 and part 2)."""
    with Path(f"inputs/{file_path}").open() as example_input_file:
        example_input = example_input_file.read()
    position, password_1, password_2 = 50, 0, 0

    for line in example_input.splitlines():
        if line[0] == "L":
            dist_to_zero, rotation = position, -int(line[1:])
        else:
            dist_to_zero, rotation = (100 - position), int(line[1:])

        if abs(rotation) % 100 == dist_to_zero:
            password_1 += 1
        if abs(rotation) >= dist_to_zero:
            password_2 += (0 if dist_to_zero == 0 else 1) + int(
                (abs(rotation) - dist_to_zero) / 100
            )
        position = (position + rotation) % 100

    return password_1, password_2
