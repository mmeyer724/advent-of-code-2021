from utils import read_input_lines, run_solution


def solution(input_name: str) -> int:
    count_increases = 0
    previous_sum = None

    input_lines = read_input_lines(input_name)

    for i in range(len(input_lines)):
        depths = map(int, input_lines[i : i + 3])
        sum_of_depths = sum(depths)

        if previous_sum is not None and sum_of_depths > previous_sum:
            count_increases += 1

        previous_sum = sum_of_depths

    return count_increases


if __name__ == "__main__":
    assert run_solution("sample.txt", func=solution) == 5
    assert run_solution("input.txt", func=solution) == 1262
