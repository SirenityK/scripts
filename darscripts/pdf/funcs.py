import os
from glob import glob

# not using pypdf because merged files are just duplicated in that package for some reason
import PyPDF2 as pypdf


def pdf_merge(name: str, dir: str, recurse: str | bool = ""):
    pwd = os.getcwd()
    if not name.endswith(".pdf"):
        name += ".pdf"
    os.chdir(dir.replace('"', ""))

    merger = pypdf.PdfWriter()
    if not recurse:
        files = glob("*.pdf")
    else:
        files = glob("**/*.pdf", recursive=True)

    files.sort()

    if name in files:
        files.remove(name)

    for i, pdf in enumerate(files):
        if not i % 5 and i != 0:
            print(f"appending {i}nth file {pdf.split()[0]}...")
        merger.append(pdf)

    print("writing...")
    os.chdir(pwd)
    merger.write(name)
    print("Done!")


if __name__ == "__main__":
    fileName = input("Enter the output file name: ")
    dir = input("Paste the directory or nothing for ./: ")
    recurse = input("Recurse? (y/n): ")

    pdf_merge(fileName, dir, recurse)
