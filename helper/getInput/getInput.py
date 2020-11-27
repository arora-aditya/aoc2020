import os
import sys

from dotenv import load_dotenv
from requests import get

YEAR = 2020

def get_cookie():
    load_dotenv()
    return os.getenv("COOKIE")

def download(url, file_name):
    cookies = {
        "session": get_cookie()
    }
    with open(file_name, "wb") as file:
        response = get(url, cookies=cookies)
        file.write(response.content)

def download_input_for_day(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    file_path = f"./day{day}/input.txt"
    download(url, file_path)
    
def get_day_from_args():
    return int(sys.argv[1])

download_input_for_day(get_day_from_args())