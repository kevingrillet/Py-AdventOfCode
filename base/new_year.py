import os.path
import re
import shutil

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

import config

COOKIES = {"session": config.SESSION}
FORCE = False
NEW = "2017"

HTTP_OK = 200


def add_day_input(year: str, d: int) -> None:
    """
    Query input of specify year & day.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    day = f"{d:02d}"
    if os.stat(f"../{year}/{day}/input").st_size != 0:
        return
    url = f"https://adventofcode.com/{year}/day/{d}"
    rq = requests.get(f"{url}/input", cookies=COOKIES)
    if rq.status_code == HTTP_OK:
        inpt = open(f"../{year}/{day}/input", "w+")
        inpt.write(rq.text)
        inpt.seek(0)
        if len(inpt.readlines()) == 1:
            replace_in_file(
                [f"../{year}/{day}/main.py"],
                [
                    ("list[str]", "str"),
                    ("# return f.read().strip()", "return f.read().strip()"),
                ],
            )
            remove_line_in_file(
                [f"../{year}/{day}/main.py"],
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
    if os.path.isfile(f"../{year}/{day}/README.md") and not FORCE:
        with open(f"../{year}/{day}/README.md") as f:
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
        data = re.sub(r" \[Twitter]\(.*\)", "", data)
        data = data.replace("[Mastodon](javascript:void(0);)] this puzzle.", "")
        data = re.sub(r"\n\s*\n", "\n\n", data)

        # Remove first line if empty
        lines = data.split("\n")
        if not lines[0].strip():
            lines = lines[1:]
        data = "\n".join(lines)

        # Save
        file = open(f"../{year}/{day}/README.md", "w")
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
    with open(f"../{year}/README.md") as f:
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
            replace_in_file([f"../{year}/README.md"], days_to_add)


def create_new_day(year: str, d: int) -> None:
    """
    Create day folder with default files.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    # Add day folder
    day = f"{d:02d}"
    if not os.path.exists(f"../{year}/{day}"):
        shutil.copytree("./day/", f"../{year}/{day}")
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
    if not os.path.exists(f"../{year}"):
        shutil.copytree("./year/", f"../{year}")

    # Set year in files
    replace_in_file([f"../{year}/README.md", f"../{year}/main.py"], [("XXXX", year)])

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
    create_new_year(NEW)
    create_new_days(NEW)
    print("Done!")
