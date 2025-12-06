import argparse
import os.path
import re
import shutil
import sys

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import config

# Base paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

COOKIES = {"session": config.SESSION}
FORCE = False

HTTP_OK = 200


def add_day_input(year: str, d: int) -> None:
    """
    Query input of specify year & day.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    day = f"{d:02d}"
    input_path = os.path.join(PROJECT_ROOT, year, day, "input")
    if os.stat(input_path).st_size != 0:
        return
    url = f"https://adventofcode.com/{year}/day/{d}"
    rq = requests.get(f"{url}/input", cookies=COOKIES)
    if rq.status_code == HTTP_OK:
        inpt = open(input_path, "w+")
        inpt.write(rq.text)
        inpt.seek(0)
        if len(inpt.readlines()) == 1:
            replace_in_file(
                [os.path.join(PROJECT_ROOT, year, day, "main.py")],
                [
                    ("list[str]", "str"),
                    ("# return f.read().strip()", "return f.read().strip()"),
                ],
            )
            remove_line_in_file(
                [os.path.join(PROJECT_ROOT, year, day, "main.py")],
                [r"return \[line\.strip\(\) for line in f\.readlines\(\)\]"],
            )
        inpt.close()
    else:
        raise NameError(f"requests.get({url}/input, cookies=COOKIES) responded with a status of: {rq.status_code}.")


def add_day_readme(year: str, d: int) -> None:
    """
    Query description of specify year & day.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    day = f"{d:02d}"
    readme_path = os.path.join(PROJECT_ROOT, year, day, "README.md")
    if os.path.isfile(readme_path) and not FORCE:
        with open(readme_path) as f:
            for line in f:
                if bool(re.search(r"Part Two", line)):
                    return

    url = f"https://adventofcode.com/{year}/day/{d}"
    rq = requests.get(url, cookies=COOKIES)
    if rq.status_code == HTTP_OK:
        soup = BeautifulSoup(rq.content, "html.parser")
        data = markdownify(str(soup.find("main")), heading_style="ATX")

        # Clean the data!
        data = data.replace(r"article \*[title]{border-bottom:1px dotted #ffff66;}", "")
        data = re.sub(
            r"At this point, all that is left is for you to \[admire your Advent calendar]\(/\d+\)\.",
            "",
            data,
        )
        data = re.sub(
            r"At this point, you should \[return to your Advent calendar]\(/\d+\) and try another puzzle\.",
            "",
            data,
        )
        data = re.sub(
            r"If you still want to see it, you can \[get your puzzle input]\(\d+/input\)\.",
            "",
            data,
        )
        data = data.replace(r"You can also [Shareon", "")
        data = data.replace(r"You can [Shareon", "")
        data = re.sub(r" \[Twitter]\(.*?\)", "", data)
        data = re.sub(r"\[Twitter]\(.*?\)", "", data)
        data = re.sub(r"\[Bluesky]\(.*?\)", "", data)
        data = data.replace("[Mastodon](javascript:void(0);)] this puzzle.", "")
        data = re.sub(r"\n\s*\n", "\n\n", data)

        # Fix relative day links to absolute URLs
        # Fix DD/input links first (e.g., ](11/input) -> absolute URL)
        data = re.sub(
            r"\]\((\d+)/input\)",
            rf"](<https://adventofcode.com/{year}/day/\1/input>)",
            data,
        )
        # Then fix simple day links (e.g., ](11) -> absolute URL)
        data = re.sub(
            r"\]\((\d+)\)",
            rf"](<https://adventofcode.com/{year}/day/\1>)",
            data,
        )
        # Fix relative /year/day/X/input links to absolute URLs
        data = re.sub(
            r"\]\(/\d+/day/(\d+)/input\)",
            rf"](<https://adventofcode.com/{year}/day/\1/input>)",
            data,
        )

        # Remove first line if empty
        lines = data.split("\n")
        if not lines[0].strip():
            lines = lines[1:]
        data = "\n".join(lines)

        # Save
        file = open(readme_path, "w")
        file.write(data)
        file.close()
    else:
        print(f"requests.get({url}) responded with a status of: {rq.status_code}.")


def add_title_readme(year: str) -> None:
    """
    Query the title of every day available and add them to the README.md.
    :param year: wanted year
    :return:
    """
    days = []
    year_readme = os.path.join(PROJECT_ROOT, year, "README.md")

    # Skip if README doesn't exist (year folder not created yet)
    if not os.path.exists(year_readme):
        return

    with open(year_readme) as f:
        for line in f:
            find = re.search(r"\[]\(<https://adventofcode.com/\d+/day/(\d+)>\)", line)
            if bool(find):
                days.append(int(find.group(1)))

    if len(days) > 0:
        days_to_add = []
        for day in days:
            url = f"https://adventofcode.com/{year}/day/{day}"
            rq = requests.get(url, cookies=COOKIES)
            if rq.status_code == HTTP_OK:
                soup = BeautifulSoup(rq.content, "html.parser")
                h2_tag = soup.find("h2")
                if h2_tag:
                    title = " ".join(h2_tag.get_text().split()[3:-1])
                    days_to_add.append(
                        (
                            f"[](<https://adventofcode.com/{year}/day/{day}>)",
                            f"[{title}](<https://adventofcode.com/{year}/day/{day}>)",
                        )
                    )
            else:
                print(f"requests.get({url}) responded with a status of: {rq.status_code}.")
                break
        if len(days_to_add) > 0:
            replace_in_file([year_readme], days_to_add)


def create_new_day(year: str, d: int) -> None:
    """
    Create day folder with default files.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    # Add day folder
    day = f"{d:02d}"
    day_path = os.path.join(PROJECT_ROOT, year, day)
    day_template = os.path.join(SCRIPT_DIR, "day")
    if not os.path.exists(day_path):
        shutil.copytree(day_template, day_path)
    add_day_input(year, d)
    add_day_readme(year, d)


def create_new_days(year: str) -> None:
    """
    Create all days for specified year.
    :param year: wanted year
    :return:
    """
    for d in range(1, 26):
        create_new_day(year, d)
        print(f'Done: Year {year} Day {f"{d:02d}"}')


def create_new_year(year: str) -> None:
    """
    Create year folder with default files.
    :param year: wanted year
    :return:
    """
    # Add year folder
    year_path = os.path.join(PROJECT_ROOT, year)
    year_template = os.path.join(SCRIPT_DIR, "year")
    if not os.path.exists(year_path):
        shutil.copytree(year_template, year_path)

        # Set year in files (only for new years)
        replace_in_file(
            [os.path.join(year_path, "README.md"), os.path.join(year_path, "main.py")],
            [("XXXX", year)],
        )

    add_title_readme(year)
    print(f"Done: Year {year}")


def remove_line_in_file(paths: list[str], matchs: list[str]) -> None:
    """
    Remove line of match in path file.
    :param matchs: list of match
    :param paths: list of paths of the files
    :return:
    """
    for path in paths:
        file = open(path)
        filedata = file.read()
        file.close()

        for match in matchs:
            filedata = re.sub(f".*{match}\n", "", filedata)

        file = open(path, "w")
        file.write(filedata)
        file.close()


def replace_in_file(paths: list[str], matchs: list[tuple[str, str]]) -> None:
    """
    Replace match with replace in path file.
    :param matchs: list of (match, replace)
    :param paths: list of paths of the files
    :return:
    """
    for path in paths:
        file = open(path)
        filedata = file.read()
        file.close()

        for match in matchs:
            filedata = filedata.replace(match[0], match[1])

        file = open(path, "w")
        file.write(filedata)
        file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Advent of Code year structure")
    parser.add_argument("year", type=str, help="Year to create (e.g., 2015)")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration of README files even if they exist",
    )
    parser.add_argument(
        "--day",
        type=int,
        help="Only create/update a specific day (1-25)",
        choices=range(1, 26),
        metavar="DAY",
    )

    args = parser.parse_args()

    # Set global FORCE flag
    FORCE = args.force

    # Create year structure
    create_new_year(args.year)

    # Create days
    if args.day:
        create_new_day(args.year, args.day)
        print(f"Done: Year {args.year} Day {args.day:02d}")
    else:
        create_new_days(args.year)

    print("Done!")
