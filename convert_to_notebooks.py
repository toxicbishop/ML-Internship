"""Convert the 4 task .py scripts into .ipynb notebooks (code-only, no docs)."""
import json
from pathlib import Path

ROOT = Path(r"D:\Code\Repo\Machine-Learning-Internship")

SCRIPTS = [
    "task1_predict_ratings.py",
    "task2_recommendation.py",
    "task3_cuisine_classification.py",
    "task4_location_analysis.py",
]


def split_cells(src: str) -> list[str]:
    """
    Split a script into cells on blank-line boundaries between top-level blocks.
    Keeps imports, each def, and the final if __name__ block as separate cells.
    """
    lines = src.splitlines(keepends=True)
    cells, buf = [], []
    i = 0
    while i < len(lines):
        line = lines[i]
        # At start of a new top-level block (no indent, not blank, not a comment-only continuation)
        stripped = line.lstrip()
        is_top_level_start = (
            line and not line.startswith((" ", "\t"))
            and stripped and not stripped.startswith("#")
        )
        # Flush buffer when we hit a new top-level def/class/if-main or the first import after non-import code
        if is_top_level_start and buf and (
            stripped.startswith(("def ", "class ", "if __name__"))
        ):
            cells.append("".join(buf).rstrip() + "\n")
            buf = []
        buf.append(line)
        i += 1
    if buf:
        cells.append("".join(buf).rstrip() + "\n")
    return cells


def make_notebook(cells_src: list[str]) -> dict:
    return {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": src.splitlines(keepends=True),
            }
            for src in cells_src
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


for name in SCRIPTS:
    src_path = ROOT / name
    dst_path = ROOT / (src_path.stem + ".ipynb")
    src = src_path.read_text(encoding="utf-8")
    cells = split_cells(src)
    nb = make_notebook(cells)
    dst_path.write_text(json.dumps(nb, indent=1), encoding="utf-8")
    print(f"{name}  ->  {dst_path.name}  ({len(cells)} cells)")
