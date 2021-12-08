import inspect
from pathlib import Path
from typing import Any, Callable, List


def _get_input_path(name: str) -> Path:
    frm = inspect.stack()[2]
    mod = inspect.getmodule(frm[0])
    return Path(mod.__file__).parent.resolve() / name


def read_input_lines(name: str) -> List[str]:
    input_path = _get_input_path(name)
    with input_path.open("r") as file:
        return list(map(lambda l: l.rstrip(), file.readlines()))


def run_solution(input_name: str, func: Callable[[str], Any]) -> Any:
    answer = func(input_name)
    print(f"Solution for {input_name}: {answer}")
    return answer
