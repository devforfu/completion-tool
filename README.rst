Prompt
======

Code completion using OpenAI's Codex. Helps to setup a simple external tool
that copies selected source file's fragment and sends it to GPT-3. The response
is inserted to the same file.

Using with PyCharm
------------------

1. Download the repo
1. Install it via `pip install .`
1. Open `Preferences > Tools > External tools > Add`
1. Configure as the screenshot shows.
1. (Optional) Bind a hotkey to invoke it, e.g. `Ctrl + X`.

![](https://github.com/devforfu/images/external_tool.png)

Now you should be able to invoke OpenAI's engine to autocomplete selected
fragment of your source file.
