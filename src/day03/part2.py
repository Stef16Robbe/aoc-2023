import math
from pathlib import Path

"""
NOTE: I didn't solve part 1. Based on lessons learned there,
I am doing part 2, but without "solving" the puzzle on the aoc website.
I just got the prompt from here: https://github.com/encse/adventofcode/blob/master/2023/Day03/README.md
So I can keep practising :).
"""


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def get_adjacents(x, y, width, height):
    out = []

    # loop over possible neighbours
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # 0,0 is ourselves, don't care
            if dx == 0 and dy == 0:
                continue

            # possible neighbour coords
            nx = x + dx
            ny = y + dy

            # check if coord exists within grid
            if nx >= 0 and nx < width and ny >= 0 and ny < height:
                out.append((nx, ny))

    return out


def main() -> None:
    # read data
    data = read_file("input.txt")

    # set up grid to work with
    grid = data.split("\n")
    width = len(grid[0])
    height = len(grid)

    stars_nums = []
    gears = {}

    t = 0
    for y in range(height):
        x = 0
        while x < width:
            # loop over all x,y coords until we find a digit
            if not grid[y][x].isdigit():
                x += 1
                continue

            # get *possible* neighbours
            checks = get_adjacents(x, y, width, height)
            num = grid[y][x]

            """
            from starting position of our number,
            move "right" on the grid until we find another number
            notice the second parameter in range(). This ensures we stay within the grid:
            """
            for i in range(x + 1, width):
                # whenever we find anything else,
                # it means we have seen all numbers in this particular sequence
                if not grid[y][i].isdigit():
                    break

                num += grid[y][i]
                # we have found a number, that means we have to check it's neighbours
                checks.extend(get_adjacents(i, y, width, height))
                # extend this loop
                x += 1

            """
            only here do we check whether the found number is actually adjacent to a symbol.
            """
            for nx, ny in checks:
                if grid[ny][nx] == "*":
                    # current problem here is that if a whole number has two or more digits
                    # adjacent to the star, it will be added as a duplicate.

                    # if the found coords of neighbours has already been added,
                    # this means we're trying to add the same number again. Don't do that.
                    # reusing some code, easier
                    a = get_adjacents(x, y, width, height)
                    if a not in stars_nums:
                        stars_nums.append(a)
                        if (nx, ny) not in gears:
                            gears[(nx, ny)] = [int(num)]
                        else:
                            gears[(nx, ny)].append(int(num))

            x += 1

    # calculate gear ratio for all found gears
    # that have exactly two part numbers adjacent
    for n in list(gears.values()):
        if len(n) == 2:
            t += math.prod(n)

    print(t)  # 81166799


if __name__ == "__main__":
    main()
