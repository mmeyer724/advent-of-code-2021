import enum
from enum import Enum
from typing import Tuple

from utils import read_input_lines, run_solution


@enum.unique
class Direction(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


def parse_command(command: str) -> Tuple[Direction, int]:
    direction_str, amount_str = command.split()
    return Direction(direction_str), int(amount_str)


def solution(input_name: str) -> int:
    current_x = 0
    current_y = 0

    for line in read_input_lines(input_name):
        direction, amount = parse_command(line)

        if direction == Direction.FORWARD:
            current_x += amount
        elif direction == Direction.DOWN:
            current_y += amount
        elif direction == Direction.UP:
            current_y -= amount

    return current_x * current_y


if __name__ == "__main__":
    run_solution("sample.txt", func=solution)
    run_solution("input.txt", func=solution)
