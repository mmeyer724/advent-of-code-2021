from utils import read_input, run_solution


def solution(input_name: str) -> int:
    count_increases = 0
    previous_depth = None

    for line in read_input(input_name):
        depth = int(line)

        if previous_depth is not None and depth > previous_depth:
            count_increases += 1

        previous_depth = depth

    return count_increases


if __name__ == "__main__":
    run_solution("day-1-sample.txt", func=solution)
    run_solution("day-1.txt", func=solution)
