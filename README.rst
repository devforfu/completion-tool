Prompt
======

Code completion using OpenAI's Codex. Helps to setup a simple external tool
that copies selected source file's fragment and sends it to GPT-3. The response
is inserted to the same file.

Using with PyCharm
------------------

#. Download the repo
#. Install it via :code:`pip install .`
#. Open :code:`Preferences > Tools > External tools > Add`
#. Configure as the screenshot shows
#. (Optional) Bind a hotkey to invoke it, e.g. :code:`Ctrl + X`

.. image:: https://github.com/devforfu/prompt/blob/master/images/external_tool.png

Now you should be able to invoke OpenAI's engine to autocomplete selected
fragment of your source file.

.. image:: https://github.com/devforfu/prompt/blob/master/images/fibonacci.gif
