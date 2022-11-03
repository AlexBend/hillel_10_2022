from pathlib import Path
from typing import Generator
import os

LESSON_4_DIR = Path(__file__).parent
TEMPFILE = LESSON_4_DIR / "temprock.txt"
ROCKYOU_FILENAME = LESSON_4_DIR / "rockyou.txt"

input_date = input()

j = []

def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


for d in filter_lines(ROCKYOU_FILENAME, input_date):
    j.append(d + "\n")

with open(TEMPFILE, "w") as file:
    file.writelines(j)


stats = os.stat(TEMPFILE)
print(stats.st_size, "bites")

with open(TEMPFILE) as file:
    size = len([0 for _ in file])
print(size, "lines")

