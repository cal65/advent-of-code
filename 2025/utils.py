import os
import re
from typing import List, Any
from pathlib import Path


def read_input(filepath, strip: bool = True) -> str:
    """Read input_data file for a specific day."""
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")

    with open(filepath, 'r') as f:
        content = f.read()

    return content.strip() if strip else content


def read_lines(filepath, strip: bool = True) -> List[str]:
    """Read input_data as list of lines."""
    content = read_input(filepath, strip)
    return content.split('\n')


def read_ints(day: int, year: int = 2024) -> List[int]:
    """Read input_data as list of integers."""
    lines = read_lines(day, year)
    return [int(line) for line in lines if line]


def read_blocks(day: int, year: int = 2024, sep: str = '\n\n') -> List[str]:
    """Read input_data as blocks separated by blank lines."""
    content = read_input(day, year, strip=False)
    return [block.strip() for block in content.split(sep)]


def read_csv(day: int, year: int = 2024, delimiter: str = ',') -> List[List[str]]:
    """Read CSV-like input_data."""
    lines = read_lines(day, year)
    return [line.split(delimiter) for line in lines]


def read_grid(day: int, year: int = 2024) -> List[List[str]]:
    """Read input_data as 2D grid."""
    lines = read_lines(day, year)
    return [list(line) for line in lines]


def manhattan_distance(p1: tuple, p2: tuple) -> int:
    """Calculate Manhattan distance between two points."""
    return sum(abs(a - b) for a, b in zip(p1, p2))


def neighbors_4(x: int, y: int, grid: List[List[Any]]) -> List[tuple]:
    """Get 4-direction neighbors (up, down, left, right)."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors


def neighbors_8(x: int, y: int, grid: List[List[Any]]) -> List[tuple]:
    """Get 8-direction neighbors (including diagonals)."""
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbors.append((nx, ny))
    return neighbors


def transpose(grid: List[List[Any]]) -> List[List[Any]]:
    """Transpose a 2D grid."""
    return [list(col) for col in zip(*grid)]


def rotate_grid(grid: List[List[Any]], clockwise: bool = True) -> List[List[Any]]:
    """Rotate a 2D grid 90 degrees."""
    if clockwise:
        return [list(reversed(col)) for col in zip(*grid)]
    else:
        return [list(col) for col in zip(*reversed(grid))]


def print_grid(grid: List[List[Any]], sep: str = ''):
    """Print a 2D grid."""
    for row in grid:
        print(sep.join(str(cell) for cell in row))


def timer(func):
    """Decorator to time function execution."""
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time: {end - start:.4f} seconds")
        return result

    return wrapper