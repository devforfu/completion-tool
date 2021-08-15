from typing import Dict

import openai

from prompt.schema import CompletionParams


def send_completion_request(prompt: str, params: CompletionParams) -> Dict:
    """Sends completion request to OpenAI completion engine and returns its response.

    The function is a small convenience wrapper on top of `openai.Completion.create`.

    Parameters
    ----------
    prompt
        Completion prompt.
    params
        Completion engine parameters.
    """
    response = openai.Completion.create(
        engine=params.engine,
        prompt=prompt,
        max_tokens=params.response_length,
        temperature=params.temperature,
        top_p=params.top_p,
        frequency_penalty=params.frequency_penalty,
        presence_penalty=params.presence_penalty,
        stop=params.stop_sequences,
        n=params.best_of,
        logprobs=params.logprobs,
        stream=params.stream,
    )
    return response
