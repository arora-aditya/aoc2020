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


def create_source_files(day: int):
    for i in range(2):
        with open(f"./day{day}/part{i+1}.py", "w") as file:
            file.write("")


def download_input_for_day(day: int):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    file_path = f"./day{day}/input.txt"
    if os.path.exists(file_path):
        return False
    download(url, file_path)
    return True


def get_day_from_args():
    return int(sys.argv[1])


day = get_day_from_args()
if download_input_for_day(day):
    create_source_files(day)
