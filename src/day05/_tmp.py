from pathlib import Path
from typing import List


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def get_new_nums(
    org: List[int], dest: tuple[int, int], src: tuple[int, int]
) -> List[int]:
    new = []

    for o in org:
        if o < src[0] and o > src[1]:
            new.append(o)
            continue

        new.append(dest[dest[0] + o])

    return new


def main() -> None:
    input = read_file("example.txt").splitlines()
    seeds = [int(i) for i in input.pop(0).split("seeds: ")[1].split(" ")]
    print(seeds)

    dest_range: tuple[int, int] = (0, 0)
    source_range: tuple[int, int] = (0, 0)

    for i, map in enumerate(input):
        print(map)
        if i == len(input) - 1:
            seeds = get_new_nums(seeds, dest_range, source_range)
            break
        if map == "":
            continue
        # this section has ended
        if not map[0].isdigit():
            if i == 1 or dest_range == 0:
                seeds = get_new_nums(seeds, dest_range, source_range)
            source_range = 0
            dest_range = 0
            continue

        val = [int(v) for v in map.split(" ")]

        dest_range.extend(list(range(val[0], val[0] + val[2])))
        source_range.extend(list(range(val[1], val[1] + val[2])))
        print(dest_range)
        print(source_range)

    print(min(seeds))


if __name__ == "__main__":
    main()
