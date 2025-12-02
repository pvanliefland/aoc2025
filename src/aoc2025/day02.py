"""Day two."""

from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Find the invalid product IDs in the gift shop database."""
    return find_invalid_ranges("day02_example.txt"), find_invalid_ranges("day02.txt")


def find_invalid_ranges(file_path: str) -> tuple[int, int]:
    """Find the invalid product IDs (parts 1 & 2)."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()
    invalid_part_1, invalid_part_2 = set(), set()

    for range_string in data.split(","):
        start, stop = range_string.split("-")
        for raw_product_id in range(int(start), int(stop) + 1):
            product_id = str(raw_product_id)
            length = len(product_id)

            if (
                length % 2 == 0
                and raw_product_id not in invalid_part_1
                and product_id[: int(length / 2)] == product_id[int(length / 2) :]
            ):
                invalid_part_1.add(raw_product_id)

            if raw_product_id not in invalid_part_2:
                for sequence_length in range(1, int(length / 2) + 1):
                    if length % sequence_length != 0:
                        continue
                    sequence = product_id[:sequence_length]
                    if product_id.count(sequence) == int(length / sequence_length):
                        invalid_part_2.add(raw_product_id)
                        continue

    return sum(invalid_part_1), sum(invalid_part_2)
