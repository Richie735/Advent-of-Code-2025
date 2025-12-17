import pathlib
import sys

# Add root to sys.path to import utils
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from utils import read_input

def solve_part1(data):
    beams = []
    splits = 0
    for line in data:
        for pos in range(len(line)):
            if (line[pos] == 'S'):
                beams.append(pos)
            elif (pos in beams) and (line[pos] == '^'):
                beams.remove(pos)
                splits += 1
                if (pos - 1 not in beams) and (pos - 1 in range(len(line))):
                    beams.append(pos - 1)
                if (pos + 1 not in beams) and (pos + 1 in range(len(line))):
                    beams.append(pos + 1)
                
    return splits

def solve_part2(data):
    # Find S
    s_row = s_col = None
    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == 'S':
                s_row, s_col = r, c
                break
        if s_row is not None: break
    if s_row is None: return 0

    R = len(data)
    C = len(data[0]) if R > 0 else 0
    memo = {}

    # Depth-First Search
    def dfs(col, row):
        if col < 0 or col >= C: return 1

        key = (col, row)
        if key in memo: return memo[key]

        # "Free Fall"
        while row < R and data[row][col] == '.': row += 1

        if row >= R:
            memo[key] = 1
            return 1
        
        if data[row][col] == '^':
            res = dfs(col - 1, row) + dfs(col + 1, row)
            memo[key] = res
            return res
        
        memo[key] = 1
        return 1

    # Start below S
    return dfs(s_col, s_row + 1)

if __name__ == "__main__":
    print("🎄 DAY 07 🎄")
    input_path = pathlib.Path(__file__).parent / "input.txt"
    data = read_input(input_path)
    data = [[c for c in line] for line in data]
    
    p1 = solve_part1(data)
    print(f"Part 1: {p1} 🎁")
    
    p2 = solve_part2(data)
    print(f"Part 2: {p2} 🌟")

