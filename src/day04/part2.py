from pathlib import Path
from typing import List


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def return_clean_nums(nums: str) -> List[int]:
    return [int(n) for n in nums.split()]


def get_matches(a: List[int], b: List[int]) -> set[int]:
    return set(a) & set(b)


def main() -> None:
    input = read_file("input.txt")

    cards = input.splitlines()
    copies = {}
    t = 0

    for i in range(len(cards) + 1):
        copies[i] = 1

    for i, card in enumerate(cards):
        card = card.split(": ")
        card.pop(0)
        card = card[0]
        splitted = card.split(" | ")
        winning_nums = return_clean_nums(splitted[0])
        our_nums = return_clean_nums(splitted[1])

        matching_nums = get_matches(winning_nums, our_nums)

        for j in range(i + 1, i + len(matching_nums) + 1):
            copies[j] += copies[i]

        t += copies[i]

    print(t)


if __name__ == "__main__":
    main()
