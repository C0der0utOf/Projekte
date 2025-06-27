import os
import time

TIMER = 10  # seconds until self-delete

print("This script will delete itself in 10 seconds...")
time.sleep(TIMER)

file = os.path.realpath(__file__)
os.remove(file)
print(f"🔥 {file} has self-destructed.")
