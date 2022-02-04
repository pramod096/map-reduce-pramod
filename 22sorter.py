# Pramod Gonegari
# Sorting

import sys

lines = sys.stdin.readlines()
lines.sort(reverse=True)

for line in lines:
    print(line)
