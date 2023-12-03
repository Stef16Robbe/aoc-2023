from pathlib import Path

"""
NOTE: THIS IS NOT MY CODE
My failed attempt can be found in `_part1.py`
I wanted to learn what a better approach would look like.
The code below is from [jmerle](https://github.com/jmerle/advent-of-code-2023/blob/master/src/day03/part1.py)
I added the comments for myself to understand his approach and how it worked, so I can learn from my mistakes :).
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
    data = read_file("example.txt")

    # set up grid to work with
    grid = data.split("\n")
    width = len(grid[0])
    height = len(grid)

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

            class range(
                __start: SupportsIndex,
                __stop: SupportsIndex,
                __step: SupportsIndex = ...,
                /
            )
            range(stop) -> range object range(start, stop[, step]) -> range object

            Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
            range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
            range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements.
            When step is given, it specifies the increment (or decrement).
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
            notice the use of `any()` here:

            (function) def any(
                __iterable: Iterable[object],
                /
            ) -> bool
            Return True if bool(x) is True for any x in the iterable.
            If the iterable is empty, return False.
            """
            if any(
                grid[ny][nx] != "." and not grid[ny][nx].isdigit() for nx, ny in checks
            ):
                t += int(num)

            x += 1

    print(t)


if __name__ == "__main__":
    main()
