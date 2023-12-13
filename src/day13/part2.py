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
