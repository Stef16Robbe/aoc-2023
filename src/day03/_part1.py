from pathlib import Path
from typing import List

"""
NOTE: this is my (failed) implementation for part 1.
It's kinda nasty and doesn't work.
I took the wrong approach by first finding the symbols, and based on that finding the numbers.
"""


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content


def print_schema(schema: List[List]) -> None:
    for i in range(len(schema[0]) + 1):
        # this is shitty but I just want it to work for now
        print(abs(i - 1), end=" ")

    print()
    for i, row in enumerate(schema):
        # https://stackoverflow.com/a/69508466/10503012
        print(f"{i} ", end="")
        # https://docs.python.org/3.10/library/stdtypes.html#str.zfill
        print(*row, sep=" ")

    print()


"""
1 0 1 2 3 4 5 6 7 8 9
0 4 6 7 . . 1 1 4 . .
1 . . . * . . . . . .
2 . . 3 5 . . 6 3 3 .
3 . . . . . . # . . .
4 6 1 7 * . . . . . .
5 . . . . . + . 5 8 .
6 . . 5 9 2 . . . . .
7 . . . . . . 7 5 5 .
8 . . . $ . * . . . .
9 . 6 6 4 . 5 9 8 . .

possible connections =
prev row -1, eq, +1
same row -1, +1
next row -1, eq, +1

so for example, take the first '*' on (4, 2)
it's adjacent numbers are 7: (3, 1), 3:  (3, 3) and 5: (4, 3)

"""

NOT_SYMBOLS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def get_symbol_pos(schema: List[List]) -> List[tuple[int, int]]:
    positions: List[tuple[int, int]] = []
    for i, col in enumerate(schema):
        for j, _ in enumerate(col):
            if schema[i][j] not in NOT_SYMBOLS:
                positions.append((int(j), int(i)))

    return positions


def check_symbol_adjacent(
    schema: List[List], symbols: List[tuple[int, int]]
) -> List[tuple[int, int]]:
    adjacent_nums = []

    for s in symbols:
        possible_positions = [
            (s[0] - 1, s[1] - 1),
            (s[0] - 1, s[1]),
            (s[0] - 1, s[1] + 1),
            (s[0], s[1] - 1),
            (s[0], s[1]),
            (s[0], s[1] + 1),
            (s[0] + 1, s[1] - 1),
            (s[0] + 1, s[1]),
            (s[0] + 1, s[1] + 1),
        ]

        for pos in possible_positions:
            try:
                if int(schema[pos[1]][pos[0]]):
                    adjacent_nums.append(pos)
            except (IndexError, ValueError):
                continue

    return adjacent_nums


# assumes given number is in the centre,
# which is obviously not the case
# doesn't work
def get_complete_number(digit: tuple[int, int], schema: List[List[str]]) -> int:
    num = str(schema[digit[1]][digit[0]])
    print(num)
    try:
        n = schema[digit[1] - 1][digit[0]]
        if int(n):
            num += n
            print(f"added {n} to {num}!")
    except (IndexError, ValueError):
        pass

    try:
        n = schema[digit[1] + 1][digit[0]]
        if int(n):
            num += n
            print(f"added {n} to {num}!")
    except (IndexError, ValueError):
        pass

    print("=====")
    return int(num)


def main() -> None:
    content = read_file("example.txt")

    total = 0

    schema = []
    for line in content.splitlines():
        schema.append(list(line))

    print_schema(schema)
    symbols = get_symbol_pos(schema)

    digits = check_symbol_adjacent(schema, symbols)
    print(digits)

    for d in digits:
        total += get_complete_number(d, schema)

    print(total)


if __name__ == "__main__":
    main()
