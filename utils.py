import pathlib
import sys

def read_input(file_path: str | pathlib.Path) -> list[str]:
    # Reads the input file and returns a list of lines, preserving empty lines.
    path = pathlib.Path(file_path)
    if not path.exists():
        print(f"Error: The puzzle input '{path}' is missing! ❄️", file=sys.stderr)
        sys.exit(1)
        
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file]