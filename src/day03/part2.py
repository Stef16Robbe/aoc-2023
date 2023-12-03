from pathlib import Path


def read_file(filename) -> str:
    path = Path(__file__).parent.resolve()
    with open(path / filename, "r") as f:
        content = f.read()
        return content


def main() -> None:
    content = read_file("example.txt")

if __name__ == "__main__":
    main()
