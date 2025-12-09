import sys
import os
import requests

YEAR = 2025
COOKIE_FILE = 'cookie.txt'

def load_cookie():
    with open(COOKIE_FILE, 'r') as infile:
        cookie = infile.readline().rstrip()
    return cookie

def fetch_input(day):
    url = f'https://adventofcode.com/{YEAR}/day/{day}/input'
    cookie = load_cookie()

    response = requests.get(url, headers={'Cookie': cookie})

    folder = f'day{day:02d}'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(f'{folder}/input.txt', 'w') as outfile:
        text = response.text.rstrip()
        outfile.write(text)
    
    print(f"🎁 Input saved to {folder}/input.txt!")

if __name__ == "__main__":
    args = sys.argv[1:]
    day = int(args[0])

    fetch_input(day)
