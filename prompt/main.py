from dataclasses import asdict
from pprint import pprint as pp

from prompt.api import send_completion_request
from prompt.cli import parse_prompt_params, parse_completion_params, parse_tool_params
from prompt.read import read_prompt
from prompt.write import write_completion


def main():
    prompt = parse_prompt_params()
    completion = parse_completion_params()
    tool = parse_tool_params()
    if tool.show_prompt:
        pp(asdict(prompt))
    string = read_prompt(prompt)
    if tool.show_prompt:
        print(string)
    result = send_completion_request(string, completion)
    if tool.show_response:
        pp(result)
    write_completion(result, prompt)


if __name__ == '__main__':
    main()
