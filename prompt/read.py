from typing import List

from prompt.schema import PromptParams


def read_prompt(params: PromptParams) -> str:
    """Reads prompt from source file.

    The prompt is copied from file starting at line `start_line` and column `start_column`,
    and ending at line `end_line` and column `end_column`.
    """
    start, end = [index - 1 for index in (params.start_line, params.end_line)]
    with open(params.filename) as f:
        lines = f.readlines()
        prompt: List[str] = []
        for i in range(start, end):
            line = lines[i]
            if i == params.start_line:
                line = line[params.start_column:]
            elif i == params.end_line:
                line = line[:params.end_column]
            prompt.append(line)
        prompt = "".join(prompt).rstrip("\n")
    return prompt
