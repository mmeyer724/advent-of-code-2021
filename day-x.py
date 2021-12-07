from utils import read_input, run_solution


def solution(input_name: str) -> int:
    for line in read_input(input_name):
        print(line)

    return 0


if __name__ == "__main__":
    run_solution("day-x-sample.txt", func=solution)
    run_solution("day-x.txt", func=solution)
