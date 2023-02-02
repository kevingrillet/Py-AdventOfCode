import os.path
import re
import shutil

import requests
from bs4 import BeautifulSoup

import config

NEW = '2017'
COOKIES = {'session': config.SESSION}


def add_day_input(year: str, d: int) -> None:
    day = "{:02d}".format(d + 1)
    if os.stat(f'../{NEW}/{day}/input').st_size != 0:
        return
    url = f'https://adventofcode.com/{NEW}/day/{d + 1}'
    rq = requests.get(f'{url}/input', cookies=COOKIES)
    if rq.status_code == 200:
        inpt = open(f'../{NEW}/{day}/input', 'w')
        inpt.write(rq.text)
        inpt.close()
    elif rq.status_code == 404:
        pass
    else:
        exit(1)


def add_title_readme(year: str) -> None:
    days = []
    with open(f'../{NEW}/README.md') as f:
        for line in f:
            find = re.search(r'\[]\(<https://adventofcode.com/\d+/day/(\d+)>\)', line)
            if bool(find):
                days.append(int(find.group(1)))

    if len(days) > 0:
        for day in days:
            url = f'https://adventofcode.com/{NEW}/day/{day}'
            rq = requests.get(url)
            if rq.status_code == 200:
                soup = BeautifulSoup(rq.content, 'html.parser')
                title = ' '.join(soup.find('h2').get_text().split()[3:-1])
                replace_in_file(f'../{NEW}/README.md', f'[](<https://adventofcode.com/{NEW}/day/{day}>)',
                                f'[{title}](<https://adventofcode.com/{NEW}/day/{day}>)')
            else:
                exit(1)


def create_new_day(year: str, d: int) -> None:
    # Add day folder
    day = "{:02d}".format(d + 1)
    if not os.path.exists(f'../{NEW}/{day}'):
        shutil.copytree('./day/', f'../{NEW}/{day}')
    add_day_input(year, d)


def create_new_days(year: str) -> None:
    for d in range(25):
        create_new_day(year, d)


def create_new_year(year: str) -> None:
    # Add year folder
    if not os.path.exists(f'../{NEW}'):
        shutil.copytree('./year/', f'../{NEW}')

    # Set year in files
    replace_in_file(f'../{NEW}/README.md', 'XXXX', NEW)
    replace_in_file(f'../{NEW}/main.py', 'XXXX', NEW)

    add_title_readme(year)


def replace_in_file(path: str, match: str, replace: str) -> None:
    file = open(path, 'r')
    filedata = file.read()
    file.close()

    newdata = filedata.replace(match, replace)

    file = open(path, 'w')
    file.write(newdata)
    file.close()


if __name__ == '__main__':
    create_new_year(NEW)
    create_new_days(NEW)
