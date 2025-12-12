import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def parse_data(data):
    for break_point in range(len(data)):
        if data[break_point] == "": break
    
    fresh_range = []
    for i in data[:break_point]:
        start, end = i.split("-")
        fresh_range.append([int(start), int(end)])

    ingredients = []
    for j in data[break_point+1:]:
        ingredients.append(int(j))

    return fresh_range, ingredients

def merge_ranges(ranges):
    bottom, top = [], []
    for b,t in ranges:
        bottom.append(b)
        top.append(t)

    bottom.sort();
    top.sort();

    m_ranges = []
    left, right = 0, 0

    while left < len(bottom):
        if right + 1 < len(bottom) and top[right] >= bottom[right+1]:
            right += 1
        
        else:
            m_ranges.append((bottom[left], top[right]))
            right += 1
            left = right

    return m_ranges

def solve_part1(fresh_range, ingredients):
    fresh, i = 0, 0

    for bot, top in fresh_range:
        while ingredients[i] < bot: i += 1
        while i < len(ingredients) and ingredients[i] <= top:
            i += 1
            fresh += 1

    return fresh

def solve_part2(fresh_range):
    fresh = 0

    for bot, top in fresh_range:
        fresh += top - bot + 1

    return fresh

if __name__ == "__main__":
    print("🎄 DAY 05 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)

    fresh_range, ingredients = parse_data(data)
    m_ranges = merge_ranges(fresh_range)
    ingredients.sort()
    
    p1 = solve_part1(m_ranges, ingredients)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(m_ranges)
    print(f"Part 2: {p2} 🌟")