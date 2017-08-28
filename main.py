# -*- coding: utf-8 -*-

"""
FIRST ADVICE
`print()` displays windows alert box.

SECOND ADVICE
It is important to check which python.exe you are running.
I don't know why but I have two python:
- C:\Program Files\Python36
- C:\Program Files\Anaconda3
I unconsciously installed pyperclip through pip (see below) with the second exe
and set the first as the python folder during Wox setup.
Check `import sys; print(sys.executable)`.

THIRD ADVICE
Run `pip install` with an Administrator Powershell.
"""

import pyperclip
import uuid
from wox import Wox

# Your class must inherit from Wox base class
class Main(Wox):

    # A function named query is necessary, we will automatically invoke this function when user query this plugin
    def query(self, key):
        u = str(uuid.uuid4())
        return [{
            "Title": u,
            "Subtitle": "Copy to clipboard",
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {
                "method": "copy_uuid",
                "parameters": [u],
                "dontHideAfterAction": False,
                },
            }]

    def copy_uuid(self, s):
        pyperclip.copy(s)

if __name__ == "__main__":
    Main()