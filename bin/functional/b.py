#!/usr/bin/python3
import clipboard
x = "(\n\t" + '\n\t.'.join(clipboard.paste().split(".")) + "\n)"
clipboard.copy(x)


