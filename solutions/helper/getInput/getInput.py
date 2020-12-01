import os
import sys

from dotenv import load_dotenv
from requests import get

YEAR = 2020


def get_cookie():
    load_dotenv()
    return os.getenv("COOKIE")


def download(url: str, file_name: str):
    cookies = {
        "session": get_cookie()
    }
    with open(file_name, "wb") as file:
        response = get(url, cookies=cookies)
        file.write(response.content)


def create_source_file(d: int):
    print('here', d)
    with open(f"day{d}.py", "w") as file:
        lines = [
            "from typing import List, Dict, Set\n",
            "from collections import defaultdict\n",
            "from functools import lru_cache\n",
            "from math import log10\n",
            "from helper.submit.submit import *\n",
            "from utils import *\n",
            "\n\n",
            f"DAY = {d}\n",
            "setup(DAY)\n",
            "file = read_file(DAY)\n",
            "\n\n",
            "# Part 1\n",
            "#"*50,
            "\nans = float(\"inf\")\n",
            "\n"*5,
            "submit(1, ans)\n"
            "\n\n",
            "# Part 2\n",
            "#"*50,
            "\nans = float(\"inf\")\n",
            "\n"*5,
            "submit(2, ans)\n"
        ]
        file.writelines(lines)


def download_input_for_day(day: int):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    file_path = f"./inputs/input{day}.txt"
    if os.path.exists(file_path):
        return False
    download(url, file_path)
    return True


def get_day_from_args():
    return int(sys.argv[1])


day = get_day_from_args()
if download_input_for_day(day):
    create_source_file(day)
else:
    print("input already exists")
