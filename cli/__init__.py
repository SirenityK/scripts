import argparse
import logging

import darscripts
from darscripts import ocr, pdf

logging.disable(logging.WARNING)


def main():
    opts = []
    for i, option in enumerate(darscripts.__all__):
        opts.append(option)
        print(f"{i+1} tools.", option.upper())

    choice = int(input("Choose an option: ")) - 1
    match choice:
        case 0:
            pdf.main()
        case 1:
            ocr.main()
        case _:
            print("Invalid choice")
            exit(1)


if __name__ == "__main__":
    main()
