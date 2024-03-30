from setuptools import find_packages, setup

required = ["pypdf2", "pdf2image", "pyperclip"]

setup(
    name="darscripts",
    version="0.1",
    packages=find_packages(),
    install_requires=[required],
    entry_points={"console_scripts": ["darscripts = cli:main"]},
    license="MIT",
    author="Dariel Fierro",
)
