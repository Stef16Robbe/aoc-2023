from pathlib import Path


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def main() -> None:
    input = read_file("example.txt")
    grid = input.split("\n")
    t = 0
    prev = ""
    print(input)
    print()
    # for i, r in enumerate(grid):
    #    if r == prev:
    #        # we have a (row) match
    #        print(f"match!: {prev} == {r}")
    #        t += (i + 1) * 100
    #        break

    #    prev = r

    # print(t)

    cols = []
    line = ""
    for y in range(len(grid)):
        if len(line) == 7:
            cols.append(line)
            line = ""
            continue

        line += grid[y][0]
    print(cols)


if __name__ == "__main__":
    main()
