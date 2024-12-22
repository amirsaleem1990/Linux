#!/home/amir/.venv_base/bin/python3
import clipboard
x = "\n".join([i for i in clipboard.paste().splitlines() if i.strip()])
# while "\n\n" in x:
# 	x = x.replace("\n\n", "\n")
clipboard.copy(x)

