from argparse import ArgumentParser
from pathlib import Path

from download import get_input

PYTHON_TEMPLATE = (
    """
from pathlib import Path


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content.strip()


def main() -> None:
    input = read_file("example.txt")


if __name__ == "__main__":
    main()

""".strip()
    + "\n"
)


def main() -> None:
    parser = ArgumentParser(description="Create skeleton files for a day.")
    parser.add_argument("day", type=int, help="the day to create files for")

    args = parser.parse_args()

    project_root = Path(__file__).parent.parent

    day_directory = project_root / "src" / f"day{args.day:02}"
    if day_directory.is_dir():
        raise RuntimeError(f"{day_directory} already exists")

    for file, content in [
        (day_directory / "example.txt", ""),
        (day_directory / "input.txt", ""),
        (day_directory / "part1.py", PYTHON_TEMPLATE),
        (day_directory / "part2.py", PYTHON_TEMPLATE),
    ]:
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("w+", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully created {file.relative_to(project_root)}")

    get_input()


if __name__ == "__main__":
    main()
