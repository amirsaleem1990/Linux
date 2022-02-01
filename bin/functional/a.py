#!/usr/bin/python3
import clipboard
x = clipboard.paste()
while "\n\n" in x:
	x = x.replace("\n\n", "\n")
clipboard.copy(x)

