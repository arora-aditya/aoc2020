import os
import re
import sys

from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
from requests import post

from termcolor import colored

YEAR = 2020
DAY = -1

URL = "https://adventofcode.com/{:d}/day/{:d}/{:s}"

RED = "red"
GREEN = "green"
BLUE = "blue"

def get_cookie():
    load_dotenv()
    return os.getenv("COOKIE")


def is_setup():
    return DAY > -1


def setup(d):
    global DAY
    DAY = d

def read_file(day):
    with open(f"./inputs/input{day}.txt", "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def set_date():
    global DAY
    global YEAR
    now = datetime.utcnow() + timedelta(hours=-5)
    y, m, d = now.year, now.month, now.day

    if m != 12 or (m == 12 and d > 25):
        print(colored("ERROR: year and day not set, and no event currently running!\n", RED))
        sys.exit(1)

    print("Year and day not set, assuming today: Dec {}, {}.\n", d, y)
    DAY = d
    YEAR = y


def check_or_die(resp):
    if resp.status_code != 200:
        print("ERROR: response {}, url: {}\n", resp.status_code, resp.url)
        print("Did you log in and update your session cookie?\n")
        sys.exit(1)

    if "please identify yourself" in resp.text.lower():
        print("ERROR: Server returned 200, but is asking for identification.\n")
        print("Did you log in and update your session cookie?\n")
        sys.exit(1)


def submit(part, answer, force=False):
    if answer == float('inf'):
        print(colored("∞ not submitted", BLUE))
        return
    
    if len(read_file(DAY)) < 50 and not force:
        print(colored(f"{answer} ==> Are you sure this isn't the sample?", RED))
        return

    if not is_setup():
        set_date()

    cookies = {
        "session": get_cookie()
    }
    data = {"level": part, "answer": answer}
    response = post(
        url=URL.format(YEAR, DAY, "answer"),
        data=data,
        cookies=cookies,
    )

    check_or_die(response)

    t = response.text.lower()

    if "did you already complete it" in t:
        print(colored(f"{answer}, Already completed!\n", GREEN))
        return True

    if "that's the right answer" in t:
        print(colored(f"{answer}, Right answer!\n", GREEN))
        return True

    if "you have to wait" in t:
        matches = re.compile(r"you have ([\w ]+) left to wait").findall(t)

        if matches:
            print(colored(f"Submitting too fast, {matches[0]} left to wait.\n", BLUE))
        else:
            print(colored("Submitting too fast, slow down!\n", BLUE))

        return False

    print(colored("Wrong answer :(\n", RED))
    return False
