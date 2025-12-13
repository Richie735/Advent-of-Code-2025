import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def parse_data(data):
    _data = [line.split() for line in data]
    nums_1 = [[int(i) for i in d] for d in _data[:-1]]

    return nums_1, _data[-1]

def solve_part1(nums, operations):
    grand_total = 0

    for x in range(len(nums[0])):
        if operations[x] == "*":
            total = 1
            for y in range(len(nums)):
                total *= nums[y][x]
            grand_total += total
        else:
            for y in range(len(nums)):
                grand_total += nums[y][x]

    return grand_total

def solve_part2(data, operations):
    cols = list(zip(*data[:-1]))

    grand_total = 0
    problems = []
    p = []

    for c in cols:
        if set(c) == {" "}:
            if p:   problems.append(p)
            p = []
        else:   p.append(c)

    if p:
        problems.append(p)

    for i, p in enumerate(problems):
        if operations[i] == "*":
            total = 1

            for num in p:
                total *= int("".join(num))

            grand_total += total
        else:
            for num in p:
                grand_total += int("".join(num))

    return grand_total

if __name__ == "__main__":
    print("🎄 DAY 06 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    with open(input_path, encoding="utf-8") as f:
        data = [line.rstrip("\n") for line in f]

    nums, operations = parse_data(data)
    
    p1 = solve_part1(nums, operations)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(data, operations)
    print(f"Part 2: {p2} 🌟")


