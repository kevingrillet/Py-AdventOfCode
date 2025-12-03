import subprocess
import time

print("== AdventOfCode XXXX")
st = time.time()
for day in range(1, 26):
    print(f"- Day {day}")
    subprocess.call(["python", "main.py"], cwd=str(day).zfill(2))
print(f"Execution time: {time.time() - st} seconds")
