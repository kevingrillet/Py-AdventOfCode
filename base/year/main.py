import subprocess
import sys
import time

print("== AdventOfCode XXXX")
st = time.time()
timings = []
for day in range(1, 26):
    print(f"- Day {day}")
    day_start = time.time()
    subprocess.call([sys.executable, "main.py"], cwd=str(day).zfill(2))
    day_time = time.time() - day_start
    timings.append((day, day_time))
    print(f"  Time: {day_time:.3f}s")

total_time = time.time() - st
print(f"\nTotal execution time: {total_time:.3f} seconds")

print("\nSlowest days:")
for day, day_time in sorted(timings, key=lambda x: x[1], reverse=True)[:5]:
    print(f"  Day {day:2d}: {day_time:.3f}s")
