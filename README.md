# 🎄 Advent of Code 2025 🎄

[![Advent of Code 2025 Banner](banner.png)](https://adventofcode.com/2025)

This repository tracks my solutions for the **[Advent of Code 2025](https://adventofcode.com/2025)** programming challenges.

## 🐍 Solutions & Structure

All solutions are implemented in **Python**.

Each day's solution is contained within its own folder (`day01`, `day02`, etc.) and includes the solution script (`solution.py`).

---

**⚠️ Important Note on Compliance:**
To adhere to the Advent of Code rules, **puzzle inputs and original problem descriptions are NOT included** in this repository. You must use your personal input downloaded from the AoC website and place it as `input.txt` within the relevant day's folder to run the solution.

Alternatively, you can use the provided helper script.

## 📥 Fetching Inputs

A helper script `get-input.py` is included to automatically download your puzzle input.

1. Get your session cookie from the Advent of Code website (inspect network requests or check storage).
2. Save the cookie string into a file named `cookie.txt` in the root directory.
3. Run the script with the day number:

```bash
python get-input.py <day>
```

For example, to fetch the input for Day 1:

```bash
python get-input.py 1
```

This will create the `day01` folder (if it doesn't exist) and save the input to `day01/input.txt`.

---

## 🏃 Getting Started

To run any solution, navigate to the specific day's folder and execute the Python script:

```bash
cd day01
python solution.py
```

---

Happy holidays and happy coding!
