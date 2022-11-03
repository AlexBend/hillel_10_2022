from pathlib import Path
from typing import Generator
import os

LESSON_4_DIR = Path(__file__).parent
TEMPROCK = LESSON_4_DIR / "temprock.txt"
ROCKYOU = LESSON_4_DIR / "rockyou.txt"

input_date = input()

coinc_list = []


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as f:
        while True:
            line = f.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


for d in filter_lines(ROCKYOU, input_date):
    coinc_list.append(d + "\n")

with open(TEMPROCK, "w") as file:
    file.writelines(coinc_list)

stats = os.stat(TEMPROCK)
print(stats.st_size, "bites")

with open(TEMPROCK) as file:
    size = len([0 for _ in file])
print(size, "lines")
