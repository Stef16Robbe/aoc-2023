from pathlib import Path
from typing import List


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def return_clean_nums(nums: str) -> List[int]:
    return [int(n) for n in nums.split()]


def get_matches(a: List[int], b: List[int]) -> int:
    return len(set(a) & set(b))


def main() -> None:
    input = read_file("input.txt")
    t = 0

    for card in input.splitlines():
        card_points = 1
        card = card.split(": ")
        card.pop(0)
        card = card[0]
        splitted = card.split(" | ")
        winning_nums = return_clean_nums(splitted[0])
        our_nums = return_clean_nums(splitted[1])

        matching_nums = get_matches(winning_nums, our_nums)
        if not matching_nums:
            continue

        for _ in range(matching_nums - 1):
            card_points *= 2

        t += card_points

    print(t)


if __name__ == "__main__":
    main()
