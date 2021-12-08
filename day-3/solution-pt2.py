from collections import Counter
from typing import List

from utils import read_input_lines, run_solution


def solution(input_name: str) -> int:
    numbers = read_input_lines(input_name)

    oxygen_rating = int(find_oxygen_rating(numbers), 2)
    co2_rating = int(find_co2_rating(numbers), 2)

    return oxygen_rating * co2_rating


def count_bits_at_position(numbers: List[str], pos: int) -> Counter:
    return Counter([number[pos] for number in numbers])


def find_oxygen_rating(numbers: List[str], current_pos: int = 0):
    if len(numbers) == 1:
        return numbers[0]

    bit_counts = count_bits_at_position(numbers, current_pos)
    most_common = "1" if bit_counts["1"] >= bit_counts["0"] else "0"

    filtered_numbers = list(filter(lambda n: n[current_pos] == most_common, numbers))

    return find_oxygen_rating(filtered_numbers, current_pos + 1)


def find_co2_rating(numbers: List[str], current_pos: int = 0):
    if len(numbers) == 1:
        return numbers[0]

    bit_counts = count_bits_at_position(numbers, current_pos)
    least_common = "0" if bit_counts["0"] <= bit_counts["1"] else "1"

    filtered_numbers = list(filter(lambda n: n[current_pos] == least_common, numbers))

    return find_co2_rating(filtered_numbers, current_pos + 1)


if __name__ == "__main__":
    run_solution("sample.txt", func=solution)
    run_solution("input.txt", func=solution)
