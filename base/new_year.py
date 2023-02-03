import os.path
import re
import shutil

import requests
from bs4 import BeautifulSoup

import config

NEW = '2017'
COOKIES = {'session': config.SESSION}


def add_day_input(year: str, d: int) -> None:
    """
    Query input of specify year & day.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    day = "{:02d}".format(d)
    if os.stat(f'../{year}/{day}/input').st_size != 0:
        return
    url = f'https://adventofcode.com/{year}/day/{d}'
    rq = requests.get(f'{url}/input', cookies=COOKIES)
    if rq.status_code == 200:
        inpt = open(f'../{year}/{day}/input', 'w')
        inpt.write(rq.text)
        inpt.close()
    else:
        raise NameError(f'requests.get({url}/input, cookies=COOKIES) responded with a status of: {rq.status_code}.')


def add_title_readme(year: str) -> None:
    """
    Query the title of every day available and add them to the README.md.
    :param year: wanted year
    :return:
    """
    days = []
    with open(f'../{year}/README.md') as f:
        for line in f:
            find = re.search(r'\[]\(<https://adventofcode.com/\d+/day/(\d+)>\)', line)
            if bool(find):
                days.append(int(find.group(1)))

    if len(days) > 0:
        for day in days:
            url = f'https://adventofcode.com/{year}/day/{day}'
            rq = requests.get(url)
            if rq.status_code == 200:
                soup = BeautifulSoup(rq.content, 'html.parser')
                title = ' '.join(soup.find('h2').get_text().split()[3:-1])
                replace_in_file(f'../{year}/README.md', f'[](<https://adventofcode.com/{year}/day/{day}>)',
                                f'[{title}](<https://adventofcode.com/{year}/day/{day}>)')
            else:
                print(f'requests.get({url}) responded with a status of: {rq.status_code}.')
                break


def create_new_day(year: str, d: int) -> None:
    """
    Create day folder with default files.
    :param year: wanted year
    :param d: wanted day (not formated on 2 characters)
    :return:
    """
    # Add day folder
    day = "{:02d}".format(d)
    if not os.path.exists(f'../{year}/{day}'):
        shutil.copytree('./day/', f'../{year}/{day}')
    add_day_input(year, d)


def create_new_days(year: str) -> None:
    """
    Create all days for specified year.
    :param year: wanted year
    :return:
    """
    for d in range(1, 26):
        create_new_day(year, d)


def create_new_year(year: str) -> None:
    """
    Create year folder with default files.
    :param year: wanted year
    :return:
    """
    # Add year folder
    if not os.path.exists(f'../{year}'):
        shutil.copytree('./year/', f'../{year}')

    # Set year in files
    replace_in_file(f'../{year}/README.md', 'XXXX', year)
    replace_in_file(f'../{year}/main.py', 'XXXX', year)

    add_title_readme(year)


def replace_in_file(path: str, match: str, replace: str) -> None:
    """
    Replace match with replace in path file.
    :param path: path of the file
    :param match: match value
    :param replace: replace value
    :return:
    """
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
