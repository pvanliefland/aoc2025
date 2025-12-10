"""Day eight."""

import math
from itertools import combinations, groupby
from pathlib import Path


def puzzle() -> tuple[tuple[int, int], tuple[int, int]]:
    """Create circuits."""
    return (connect_some("day08_example.txt", 10), connect_all("day08_example.txt")), (
        (connect_some("day08.txt", 1000), connect_all("day08.txt"))
    )


def connect_some(file_path: str, max_conn: int) -> int:
    """Connect some circruits."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    boxes = {tuple(map(int, row.split(","))): None for row in data.splitlines()}
    distances = {}
    connections = 0
    circuit_id = 0

    pairs = list(combinations(boxes, 2))
    for pair in pairs:
        distances[pair] = distance(pair[0], pair[1])

    while connections < max_conn:
        (closest_pair, _closest_distance) = min(distances.items(), key=lambda i: i[1])
        distances.pop(closest_pair)

        # Case 1: b1 part of circuit, b2 not -> b2 part of circuit of b1
        if boxes[closest_pair[0]] is not None and boxes[closest_pair[1]] is None:
            boxes[closest_pair[1]] = boxes[closest_pair[0]]
            connections += 1
        # Case 2: b0 not part of circuit, b1 part of circuit -> b1 part of circuit of b2
        elif boxes[closest_pair[1]] is not None and boxes[closest_pair[0]] is None:
            boxes[closest_pair[0]] = boxes[closest_pair[1]]
            connections += 1
        # Case 3: both are part of circuit -> merge circuit of b2 in circuit of b1
        elif boxes[closest_pair[0]] is not None and boxes[closest_pair[1]] is not None:
            to_keep = boxes[closest_pair[0]]
            to_merge = boxes[closest_pair[1]]
            if to_keep != to_merge:
                for k, v in boxes.items():
                    if v == to_merge:
                        boxes[k] = to_keep
            connections += 1
        # Case 4: new circuit
        else:
            boxes[closest_pair[0]] = circuit_id
            boxes[closest_pair[1]] = circuit_id
            circuit_id += 1
            connections += 1

    values = sorted(c for c in boxes.values() if c is not None)
    grouped = sorted([len(list(group[1])) for group in groupby(values)], reverse=True)
    _others = list({k for k, v in boxes.items() if v is None})

    return math.prod(grouped[:3])


def connect_all(file_path: str) -> int:
    """Connect all circruits."""
    with Path(f"inputs/{file_path}").open() as input_file:
        data = input_file.read()

    boxes = {tuple(map(int, row.split(","))): None for row in data.splitlines()}
    distances = {}
    connections = 0
    circuit_id = 0

    pairs = list(combinations(boxes, 2))
    for pair in pairs:
        distances[pair] = distance(pair[0], pair[1])

    while any(c is None for b, c in boxes.items()):
        (closest_pair, _closest_distance) = min(distances.items(), key=lambda i: i[1])
        distances.pop(closest_pair)

        # Case 1: b1 part of circuit, b2 not -> b2 part of circuit of b1
        if boxes[closest_pair[0]] is not None and boxes[closest_pair[1]] is None:
            boxes[closest_pair[1]] = boxes[closest_pair[0]]
            connections += 1
        # Case 2: b0 not part of circuit, b1 part of circuit -> b1 part of circuit of b2
        elif boxes[closest_pair[1]] is not None and boxes[closest_pair[0]] is None:
            boxes[closest_pair[0]] = boxes[closest_pair[1]]
            connections += 1
        # Case 3: both are part of circuit -> merge circuit of b2 in circuit of b1
        elif boxes[closest_pair[0]] is not None and boxes[closest_pair[1]] is not None:
            to_keep = boxes[closest_pair[0]]
            to_merge = boxes[closest_pair[1]]
            if to_keep != to_merge:
                for k, v in boxes.items():
                    if v == to_merge:
                        boxes[k] = to_keep
            connections += 1
        # Case 4: new circuit
        else:
            boxes[closest_pair[0]] = circuit_id
            boxes[closest_pair[1]] = circuit_id
            circuit_id += 1
            connections += 1

    return closest_pair[0][0] * closest_pair[1][0]


def distance(p: tuple[int, int, int], q: tuple[int, int, int]) -> float:
    """Calculate the distance."""
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2) ** 1 / 2
