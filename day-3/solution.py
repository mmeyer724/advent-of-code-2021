from collections import defaultdict
from typing import Dict

from utils import read_input_lines, run_solution


def solution(input_name: str) -> int:
    input_lines = read_input_lines(input_name)
    counts_by_position: Dict[int, int] = defaultdict(int)

    for line in input_lines:
        for pos, value in enumerate(line):
            counts_by_position[pos] += 1 if value == "1" else 0

    num_bits = len(counts_by_position.keys())
    gamma_rate = 0
    epsilon_rate = 0

    for pos, count in counts_by_position.items():
        mask = 1 << (num_bits - pos - 1)
        if count >= len(input_lines) / 2:
            gamma_rate |= mask
        else:
            epsilon_rate |= mask

    return gamma_rate * epsilon_rate


if __name__ == "__main__":
    run_solution("sample.txt", func=solution)
    run_solution("input.txt", func=solution)
