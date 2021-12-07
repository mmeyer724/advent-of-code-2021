from utils import read_input_lines, run_solution


def solution(input_name: str) -> int:
    count_increases = 0
    previous_depth = None

    for line in read_input_lines(input_name):
        depth = int(line)

        if previous_depth is not None and depth > previous_depth:
            count_increases += 1

        previous_depth = depth

    return count_increases


if __name__ == "__main__":
    assert run_solution("sample.txt", func=solution) == 7
    assert run_solution("input.txt", func=solution) == 1292
