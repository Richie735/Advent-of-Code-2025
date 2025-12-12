import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def check_neighbors (matrix, y, x):
    rolls = 0

    for dy in range (-1, 2):
        for dx in range (-1, 2):
            if (dx, dy) == (0, 0): continue
            
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]):
                if matrix[ny][nx] == "@":
                    rolls += 1

    return (rolls < 4)

def solve_part1(data):
    accessible = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            if (data[y][x] == '.'): continue
            elif (check_neighbors(data,y,x)): accessible += 1

    return accessible

def solve_part2(data):
    removed = 0
    iteration_removed = 1

    while iteration_removed != 0:
        iteration_removed = 0

        for y in range(len(data)):
            for x in range(len(data[0])):
                if (data[y][x] != '@'): continue
                elif (check_neighbors(data,y,x)): 
                    data[y][x] = 'X'
                    iteration_removed += 1
        
        removed += iteration_removed

    return removed

if __name__ == "__main__":
    print("🎄 DAY 04 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)

    matrix = []
    for line in data:
        matrix.append([pos for pos in line]);
    
    p1 = solve_part1(matrix)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(matrix)
    print(f"Part 2: {p2} 🌟")
