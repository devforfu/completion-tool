from typing import Dict

from prompt.schema import PromptParams


def write_completion(response: Dict, params: PromptParams) -> None:
    """Writes prompt's completion back to source file.

    The completion is inserted between the last prompt's line and the rest of
    file content.

    Parameters
    ----------
    response
        Completion response.
    params
        Prompt parameters.
    """
    completion = response["choices"][0]["text"]
    with open(params.filename) as f:
        lines = f.readlines()
    lines.insert(params.end_line, completion)
    with open(params.filename, "w") as f:
        f.writelines(lines)
