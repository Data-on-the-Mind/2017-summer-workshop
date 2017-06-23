import os
import glob

from nbformat import read, write, current_nbformat
from nbconvert.preprocessors import ClearOutputPreprocessor

notebooks = glob.glob("*/*.ipynb")
for nbpath in notebooks:
    print(nbpath)

    with open(nbpath, "r") as fh:
        nb = read(fh, current_nbformat)

    for cell in nb.cells:
        cell.metadata = {}

    nb, _ = ClearOutputPreprocessor().preprocess(nb, {})
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    }

    with open(nbpath, "w") as fh:
        write(nb, fh, current_nbformat)
