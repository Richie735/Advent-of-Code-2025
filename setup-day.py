import sys
import os
import requests

YEAR = 2025
COOKIE_FILE = 'cookie.txt'
TEMPLATE = """import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def solve_part1(data):
    # Solves Part 1
    # TODO: Help the elves! 🧝
    return 0

def solve_part2(data):
    # Solves Part 2
    # TODO: Save Christmas! 🎅
    return 0

if __name__ == "__main__":
    print("🎄 DAY {day:02d} 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)
    
    p1 = solve_part1(data)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(data)
    print(f"Part 2: {p2} 🌟")
"""

def load_cookie():
    with open(COOKIE_FILE, 'r') as infile:
        cookie = infile.readline().rstrip()
    return cookie

def setup_day(day):
    url = f'https://adventofcode.com/{YEAR}/day/{day}/input'
    cookie = load_cookie()

    response = requests.get(url, headers={'Cookie': cookie})

    folder = f'day{day:02d}'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(f'{folder}/input.txt', 'w', encoding='utf-8') as outfile:
        text = response.text.rstrip()
        outfile.write(text)
    
    solution_path = f'{folder}/solution.py'
    if not os.path.exists(solution_path):
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(TEMPLATE.replace("{day:02d}", f"{day:02d}"))
            
    print(f"🎄 Day {day} setup complete! 🎁")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Please provide the day number.")
        sys.exit(1)
        
    day = int(args[0])

    setup_day(day)
