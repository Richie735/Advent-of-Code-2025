import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def solve_part1(data):
    jolted = 0 

    for bank in data:
        left = 0

        for i in range(len(bank) - 1):
            if bank[i] > bank[left]:
                left = i

        right = left + 1
        for i in range(left + 1, len(bank)):
            if bank[i] > bank[right]: 
                right = i

        jolted += (int(bank[left]) * 10) + int(bank[right])

    return jolted

def solve_part2(data):
    total_joltage = 0 

    for bank in data:
        current = 0
        jolted = ""
        
        for i in range(12, 0, -1):
            end_search = len(bank) - (i - 1)
            window = bank[current : end_search]
            
            nr = max(window)
            
            jolted += nr
            current += window.index(nr) + 1
        
        total_joltage += int(jolted)

    return total_joltage

if __name__ == "__main__":
    print("🎄 DAY 03 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)
    
    p1 = solve_part1(data)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(data)
    print(f"Part 2: {p2} 🌟")
