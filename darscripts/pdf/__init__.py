from darscripts.pdf.funcs import pdf_merge
from darscripts.utils import TODO, basic_inputs, menu

options = {
    "Merge all files from a directory": lambda: pdf_merge(**basic_inputs()),
    "Encrypt a PDF file": TODO,
    "Decrypt a PDF file": TODO,
    "Split a PDF file": TODO,
    "Extract images from a PDF file": TODO,
    "Extract text from a PDF file": TODO,
    "Compress a PDF file": TODO,
    "Convert a PDF file to an image": TODO,
    "Convert an image to a PDF file": TODO,
}


def main():
    menu(options)
