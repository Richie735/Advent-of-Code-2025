import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def solve_part1(data):
    dial = 50
    password = 0

    for line in data:
        direction = line[0]
        rotations = int(line[1:])

        if direction == "R":
            dial = (dial + rotations) % 100
        else:
            dial = (dial - rotations) % 100
        
        if dial == 0:
            password += 1
            
    return password

def solve_part2(data):
    dial = 50
    password = 0
    
    for line in data:
        direction = line[0]
        rotations = int(line[1:])

        if direction == "R":
            password += (dial + rotations) // 100
            dial = (dial + rotations) % 100
        else:
            password += (dial - 1) // 100 - (dial - rotations - 1) // 100
            dial = (dial - rotations) % 100
            
    return password

if __name__ == "__main__":
    print("🎄 DAY 01 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)
    
    p1 = solve_part1(data)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(data)
    print(f"Part 2: {p2} 🌟")
