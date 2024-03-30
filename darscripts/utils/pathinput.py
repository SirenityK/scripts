import os
import platform
from typing import Dict, Union


def basic_inputs(
    name=True, dir=True, recurse: str | bool = "ask"
) -> Dict[str, Union[str, bool]]:
    res = {}
    if name:
        res["name"] = input("Enter the output file name: ")
    if dir:
        res["dir"] = input("Paste the directory or nothing for ./: ")
    else:
        res["dir"] = os.getcwd() + "\\" if platform.system() == "Windows" else "/"
    if recurse:
        res["recurse"] = True if input("Recurse? (y/n): ").lower() == "y" else False

    return res


if __name__ == "__main__":
    print(basic_inputs())
