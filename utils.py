from pathlib import Path
from typing import Any, Callable, Iterator

PARENT_DIR = Path(__file__).parent.resolve()
INPUTS_DIR = Path(PARENT_DIR / "inputs")


def read_input(name: str, rstrip=True) -> Iterator[str]:
    input_path = INPUTS_DIR / name

    with input_path.open("r") as file:
        while line := file.readline():
            if rstrip:
                yield line.rstrip()
            else:
                yield line


def run_solution(input_name: str, func: Callable[[str], Any]):
    print(f"Solution for {input_name}: {func(input_name)}")
