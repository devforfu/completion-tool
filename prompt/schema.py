from dataclasses import dataclass, field
from typing import List


@dataclass
class CompletionParams:
    """Completion engine parameters.

    Parameters
    ----------
    engine (str, default: davinci-codex)
    response_length (int, default: 256)
    temperature (float, default: 0.7)
    top_p (int, default: 1)
    frequency_penalty (float, default: 0)
    presence_penalty (float, default: 0)
    best_of (int, default: 1)
    stop_sequences (List[str], default: ["def", "class"])
    logprobs (int, default: None)
    stream (bool, default: False)
    """
    engine: str = "davinci-codex"
    response_length: int = 256
    temperature: float = 0.7
    top_p: int = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0
    best_of: int = 1
    stop_sequences: List[str] = field(default_factory=lambda: ["def", "class"])
    logprobs: int = None
    stream: bool = False


@dataclass
class PromptParams:
    """Prompt configuring parameters.

    Parameters
    ----------
    filename (str, required)
        Path to a source file where input prompt is taken from.
    start_line (int, required)
        Line number where the prompt starts.
    end_line (int, required)
        Line number where the prompt ends.
    start_column (int, default: 0)
        Column number where the prompt starts.
    end_column (int, default: 0)
        Column number where the prompt ends.
    """
    filename: str
    start_line: int
    end_line: int
    start_column: int = 0
    end_column: int = 0


@dataclass
class ToolParams:
    """CLI tool configuration parameters.

    Parameters
    ----------
    show_prompt
        If True, prints the selected prompt to stdout.
    show_response
        If True, prints the response to stdout.
    """
    show_prompt: bool = True
    show_response: bool = True
