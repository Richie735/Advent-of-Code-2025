import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def solve_part1(data):
    total = 0

    for r in data:
        start, end = map(int, r.split('-'))
        
        for i in range(start, end + 1):
            id = str(i)

            if (len(id) % 2 == 1):   continue

            half = len(id) // 2
            if (id[half:] == id[:half]):
                total += i
            
    return total

def solve_part2(data):
    total = 0

    for r in data:
        start, end = map(int, r.split('-'))
        
        for i in range(start, end + 1):
            id = str(i)

            if id in (id + id)[1:-1]: total += i

    return total

if __name__ == "__main__":
    print("🎄 DAY 02 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)

    data = data[0].split(',')
    
    p1 = solve_part1(data)
    print(f"Part 1: {p1} 🎁")

    p2 = solve_part2(data)
    print(f"Part 2: {p2} 🌟")
