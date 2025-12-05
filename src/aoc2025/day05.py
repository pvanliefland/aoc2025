"""Day five."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Find out how many products are fresh (in practice and in theory)."""
    return (fresh_products("day05_example.txt"), fresh_products("day05.txt"))


def fresh_products(file_path: str) -> tuple[int, int]:
    """Count fresh products."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    fresh_data, available_data = data.split("\n\n")
    fresh = []
    for fresh_row in fresh_data.splitlines():
        start, stop = fresh_row.split("-")
        fresh.append(range(int(start), int(stop) + 1))
    available = [int(a) for a in available_data.splitlines()]

    fresh_and_clean = []
    last_stop = 0
    for fresh_range in sorted(fresh, key=lambda r: r.start):
        start = max(last_stop, fresh_range.start)
        if fresh_range.stop > start:
            fresh_and_clean.append(range(start, last_stop := fresh_range.stop))

    return (
        len([p for p in available if any(p in r for r in fresh_and_clean)]),
        sum(len(r) for r in fresh_and_clean),
    )
