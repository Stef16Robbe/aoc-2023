from __future__ import annotations

import sys
from enum import Enum
from pprint import pformat
from typing import List


class Cube:
    class Color(Enum):
        Red = "red"
        Green = "green"
        Blue = "blue"

    def __init__(self, amount: int, color: str) -> None:
        self.amount = amount
        self.color = self.Color(color)

    def __repr__(self):
        return pformat(vars(self), indent=4, width=1)


class Set:
    RED_MAX = 12
    GREEN_MAX = 13
    BLUE_MAX = 14

    def __init__(self, cubes: List[Cube]) -> None:
        self.cubes = cubes
        self.amounts = {Cube.Color.Red: 0, Cube.Color.Green: 0, Cube.Color.Blue: 0}

    def __repr__(self):
        return pformat(vars(self), indent=4, width=1)

    def possible(self) -> bool:
        if (
            self.amounts[Cube.Color.Red] <= self.RED_MAX
            and self.amounts[Cube.Color.Green] <= self.GREEN_MAX
            and self.amounts[Cube.Color.Blue] <= self.BLUE_MAX
        ):
            return True
        return False

    @classmethod
    def from_str(cls, s) -> Set:
        cubes: List[Cube] = []

        for cube in s.split(", "):
            values = cube.split(" ")
            c = Cube(int(values[0]), values[1])
            cubes.append(c)

        return Set(cubes)


class Game:
    def __init__(self, id: int, sets: List[Set]) -> None:
        self.id = id
        self.sets = sets
        self.highest = {Cube.Color.Red: 1, Cube.Color.Green: 1, Cube.Color.Blue: 1}

    def __repr__(self):
        return pformat(vars(self), indent=4, width=1)

    @classmethod
    def from_str(cls, s) -> Game:
        sets: List[Set] = []
        splitted = s.split(": ")
        id = int(splitted.pop(0).split(" ")[1])

        for set in splitted[0].split("; "):
            sets.append(Set.from_str(set))

        return Game(id, sets)


def main() -> None:
    input = sys.stdin.read().strip()

    id_count = 0

    for line in input.splitlines():
        set_possible = True
        game = Game.from_str(line)
        for s in game.sets:
            for cube in s.cubes:
                s.amounts[cube.color] += cube.amount

            if not s.possible():
                set_possible = False
                break

        if set_possible:
            id_count += game.id

    print(id_count)


if __name__ == "__main__":
    main()
