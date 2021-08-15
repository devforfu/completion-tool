from argparse import ArgumentParser

from prompt.schema import CompletionParams, PromptParams, ToolParams


def parse_completion_params() -> CompletionParams:
    """Creates argument parser for completion parameters.

    The function tries to parse only the known parameters and returns
    a dataclass initialized with parsed values.

    Returns
    -------
    CompletionParams
        The parsed parameters

    """
    parser = ArgumentParser()
    parser.add_argument(
        "--engine",
        default="davinci-codex",
        help="Completion engine",
    )
    parser.add_argument(
        "--response-length",
        default=256,
        type=int,
        help="Maximum length of the response. (default: 256)",
    )
    parser.add_argument(
        "--temperature",
        default=0.7,
        type=float,
        help="Sampling softmax temperature. (default: 0.7)",
    )
    parser.add_argument(
        "--top-p",
        default=1,
        type=int,
        help="Nucleus filtering (top-p) before sampling (<=0.0: no filtering). (default: 1)",
    )
    parser.add_argument(
        "--frequency-penalty",
        default=0,
        type=float,
        help="Frequency penalty for beam search. (default: 0)",
    )
    parser.add_argument(
        "--presence-penalty",
        default=0,
        type=float,
        help="Presence penalty for beam search. (default: 0)",
    )
    parser.add_argument(
        "--best-of",
        default=1,
        type=int,
        help="Number of best completions to output. (default: 1)",
    )
    parser.add_argument(
        "--stop-sequences",
        default=["def", "class"],
        nargs="+",
        help="Stop completions on these sequences. (default: ['def', 'class'])",
    )
    parser.add_argument(
        "--logprobs",
        default=None,
        type=int,
        help="Print N logprobs. Has priority over --stream. (default: None)",
    )
    parser.add_argument(
        "--stream",
        default=False,
        type=bool,
        help="Stream output. (default: False)",
    )
    args, _ = parser.parse_known_args()
    return CompletionParams(**vars(args))


def parse_prompt_params() -> PromptParams:
    """Creates argument parser for prompt parameters.

    The function tries to parse only the known parameters and returns
    a dataclass initialized with parsed values.

    Returns
    -------
    PromptParams
        The parsed parameters
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--filename",
        required=True,
        help="Path to a source file where input prompt is taken from.",
    )
    parser.add_argument(
        "--start-line",
        required=True,
        type=int,
        help="Line number where the prompt starts.",
    )
    parser.add_argument(
        "--end-line",
        required=True,
        type=int,
        help="Line number where the prompt ends.",
    )
    parser.add_argument(
        "--start-column",
        default=0,
        type=int,
        help="Column number where the prompt starts. (default: 0)",
    )
    parser.add_argument(
        "--end-column",
        default=0,
        type=int,
        help="Column number where the prompt ends. (default: 0)",
    )
    args, _ = parser.parse_known_args()
    return PromptParams(**vars(args))


def parse_tool_params() -> ToolParams:
    """Creates argument parser for tool parameters.

    Returns
    -------
    ToolParams
        Parsed tool parameters.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--show-prompt",
        default=True,
        type=bool,
        help="Print the prompt to stdout. (default: True)",
    )
    parser.add_argument(
        "--show-response",
        default=True,
        type=bool,
        help="Print the response to stdout. (default: True)",
    )
    args, _ = parser.parse_known_args()
    return ToolParams(**vars(args))
