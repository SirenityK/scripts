import io
from glob import glob

import pdf2image
import pyperclip as p
from utils import basic_inputs

inputs = basic_inputs()
if inputs["recurse"]:
    files = glob(inputs["dir"] + "**/*.pdf", recursive=True)
else:
    files = glob(inputs["dir"] + "*.pdf")

for file in files:
    with open(file, "rb") as f, io.BytesIO() as output:
        images = pdf2image.convert_from_bytes(f.read())
        for i, image in enumerate(images):
            image.save(output, format="PNG")
            p.copy(output.getvalue())
            print(f"Copied page {i+1} of {file}")
