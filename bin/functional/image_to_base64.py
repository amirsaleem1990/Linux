#!/home/amir/.venv_base/bin/python3

import base64
import clipboard

# Specify the path to your PNG file
file_path = 'image.png'

# Read the file in binary mode
with open(file_path, 'rb') as image_file:
    # Convert to base64
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

clipboard.copy(base64_string)
print("\n\n>>>>>>> Copied to clipboard\n")