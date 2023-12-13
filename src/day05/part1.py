import sys
from pathlib import Path
from typing import List


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def main() -> None:
    input = read_file("input.txt").split("\n")
    input = list(filter(None, input))
    seeds = [int(i) for i in input.pop(0).split("seeds: ")[1].split(" ")]

    tmp = []
    maps = []
    for section in input:
        if not section[0].isdigit():
            if len(tmp) > 0:
                maps.append(tmp)
                tmp = []
            continue

        dest, src, length = [int(v) for v in section.split(" ")]
        tmp.append((dest, src, length))

    lowest = sys.maxsize
    for seed in seeds:
        curr = seed
        for map in maps:
            for m in map:
                if m[1] <= curr < m[1] + m[2]:
                    curr = m[0] + (curr - m[1])
                    break

        lowest = min(lowest, curr)

    print(lowest)


if __name__ == "__main__":
    main()
