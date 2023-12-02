import sys

all_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


# find ALL occurences of substring in string
# improvement of builtin str.find()
# thanks SO (https://stackoverflow.com/a/4665027/10503012)
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub) or 1  # use start += 1 to find overlapping matches


def get_digit_positions(line: str) -> {}:
    # 1. find all numbers in line
    # 2. get their positions
    # 3. important note: USING str.find() MEANS ASSUMING EACH DIGIT IS ONLY PRESENT ONCE!!!
    digits = {}
    for d in all_digits:
        if d in line:
            for found in list(find_all(line, d)):
                # starting position: digit
                digits[found] = d

    # return sorted based on starting position
    return dict(sorted(digits.items()))


def main() -> None:
    input = sys.stdin.read().strip()

    total = 0
    for line in input.splitlines():
        sorted_line_digits = get_digit_positions(line)
        # we now have all digits and their starting positions
        # we want the digit(s) with the lowest and highest starting position
        # and convert word digits & strings to actual ints:

        templist = list(sorted_line_digits.values())
        first, last = (
            templist[0],
            templist[-1],
        )

        total += int(all_digits[first] + all_digits[last])

    print(total)


if __name__ == "__main__":
    main()
