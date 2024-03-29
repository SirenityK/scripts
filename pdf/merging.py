import os
from glob import glob

import PyPDF2 as pypdf


def pdf_merge(outName: str, dir: str, recurse: str | bool = False):
    recurse = True if recurse.lower() == "y" else False
    if not outName.endswith(".pdf"):
        outName += ".pdf"
    os.chdir(dir.replace('"', ""))

    merger = pypdf.PdfWriter()
    if not recurse:
        files = glob("*.pdf")
    else:
        files = glob("**/*.pdf", recursive=True)

    if outName in files:
        files.remove(outName)

    for i, pdf in enumerate(files):
        if not i % 5 and i != 0:
            print(f"appending {i}nth file {pdf.split()[0]}...")
        merger.append(pdf)

    print("writing...")
    merger.write(outName)
    print("Done!")


if __name__ == "__main__":
    name = input("Enter the output file name: ")
    dir = input("Paste the directory or nothing for ./: ")
    recurse = input("Recurse? (y/n): ")

    pdf_merge(name, dir, recurse)
