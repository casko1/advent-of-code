import re
from collections import defaultdict

lines = open("7.txt").readlines()[::2]
counts = defaultdict(int)
counts[lines[0].index("S")] += 1
p1 = 0

for i, line in enumerate(lines[1:]):
    splitter_positions = [m.start() for m in re.finditer(r"\^", line)]

    p1 += len([k for k, v in counts.items() if v > 0 and k in splitter_positions])

    for p, n in list(counts.items()):
        if p in splitter_positions:
            counts[p] = 0
            counts[p + 1] += n
            counts[p - 1] += n

print(p1, sum(counts.values()))
