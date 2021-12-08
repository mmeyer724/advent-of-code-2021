from dataclasses import dataclass
from typing import List, Set, Tuple

from utils import read_input_lines, run_solution


@dataclass
class Gameboard:
    rows: List[Set[int]]
    cols: List[Set[int]]

    def calculate_score(self, called_numbers: Set[int], last_number: int) -> int:
        all_numbers = set()
        for row in self.rows:
            all_numbers.update(row)
        for col in self.cols:
            all_numbers.update(col)

        unmarked_numbers = all_numbers - called_numbers

        return sum(unmarked_numbers) * last_number

    def check_win(self, called_numbers: Set[int]) -> bool:
        # Check all horizontal rows of the gameboard
        if any(called_numbers.issuperset(row) for row in self.rows):
            return True

        # Check all vertical columns of the gameboard
        if any(called_numbers.issuperset(col) for col in self.cols):
            return True

        return False


def parse_input(input_lines: List[str]) -> Tuple[List[int], List[Gameboard]]:
    """
    This function parses the provided input lines and returns a tuple
    containing the list of numbers to be called and a list of gameboard objects.
    """
    numbers = list(map(int, input_lines[0].split(",")))
    gameboards: List[Gameboard] = []

    for idx in range(2, len(input_lines), 6):
        gb_lines = input_lines[idx : idx + 5]
        parsed_rows = [list(map(int, gb_line.split())) for gb_line in gb_lines]

        gb_rows = [set(row) for row in parsed_rows]
        gb_cols = [
            set(row[idx] for row in parsed_rows)
            for idx in range(0, len(parsed_rows[0]))
        ]

        gameboards.append(Gameboard(rows=gb_rows, cols=gb_cols))

    return numbers, gameboards


def solution(input_name: str) -> int:
    input_lines = read_input_lines(input_name)
    all_numbers, gameboards = parse_input(input_lines)

    called_numbers = set()

    for number in all_numbers:
        called_numbers.add(number)
        for gameboard in gameboards:
            if gameboard.check_win(called_numbers):
                return gameboard.calculate_score(called_numbers, number)

    return -1


if __name__ == "__main__":
    assert run_solution("sample.txt", func=solution) == 4512
    assert run_solution("input.txt", func=solution) == 32844
