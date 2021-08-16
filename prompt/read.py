from typing import List

from prompt.schema import PromptParams


def read_prompt(params: PromptParams) -> str:
    """Reads prompt from source file.

    The prompt is copied from file starting at line `start_line` and column `start_column`,
    and ending at line `end_line` and column `end_column`.
    """
    start_line, end_line, start_column, end_column = decrement([
        params.start_line,
        params.end_line,
        params.start_column,
        params.end_column
    ])
    with open(params.filename) as f:
        lines = f.readlines()
        prompt: List[str] = []
        for i in range(start_line, end_line):
            line = lines[i]
            if i == params.start_line:
                line = line[start_column:]
            elif i == params.end_line:
                line = line[:end_column]
            prompt.append(line)
        prompt = "".join(prompt).rstrip("\n")
    return prompt


def decrement(values: List[int]) -> List[int]:
    """Decrements each value in list."""

    return [v - 1 for v in values]
