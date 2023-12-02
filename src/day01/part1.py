import sys


def main() -> None:
    input = sys.stdin.read().strip()

    total = 0
    for line in input.splitlines():
        ordered_digits = list(filter(str.isdigit, line))
        total += int(ordered_digits[0] + ordered_digits[-1])

    print(total)


if __name__ == "__main__":
    main()
