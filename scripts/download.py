import os
from argparse import ArgumentParser
from pathlib import Path

from dotenv import load_dotenv
from requests import Session


def get_requests_session() -> Session:
    session = Session()
    session.headers.update(
        {
            "User-Agent": "https://github.com/Stef16Robbe/aoc-2023 by stef.robbe@gmail.com"
        }
    )

    load_dotenv()
    session.cookies.set("session", os.environ["SESSION_COOKIE"])

    return session


def get_input() -> None:
    parser = ArgumentParser(description="Download input data for a day.")
    parser.add_argument("day", type=int, help="the day to download input data for")

    args = parser.parse_args()

    project_root = Path(__file__).parent.parent

    input_file = project_root / "src" / f"day{args.day:02}" / "input.txt"
    if not input_file.is_file():
        raise RuntimeError(f"{input_file} does not exist")

    input_response = get_requests_session().get(
        f"https://adventofcode.com/2023/day/{args.day}/input"
    )
    input_response.raise_for_status()

    input_file.write_text(input_response.text, encoding="utf-8")
    print(f"Successfully wrote input data to {input_file.relative_to(project_root)}")
