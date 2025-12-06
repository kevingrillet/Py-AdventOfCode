import subprocess
import sys
import time

print("== AdventOfCode 2015")
st = time.time()
for day in range(1, 26):
    print(f"- Day {day}")
    subprocess.call([sys.executable, "main.py"], cwd=str(day).zfill(2))
print(f"Execution time: {time.time() - st} seconds")
