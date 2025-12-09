import math
from itertools import combinations

lines = open("8.txt").readlines()

nodes = []
distances = []


def distance(n1, n2):
    return math.sqrt((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2 + (n1[2] - n2[2]) ** 2)


for line in lines:
    a, b, c = line.split(",")
    nodes.append((int(a), int(b), int(c)))

for (i, c1), (j, c2) in combinations(enumerate(nodes), 2):
    d = distance(c1, c2)
    distances.append((i, j, d))

distances = sorted(distances, key=lambda tup: tup[2])

groups = {n: {n} for n in range(len(nodes))}

for i in range(100000):
    a, b, d = distances.pop(0)

    if i == 1000:
        # TIL frozenset makes set hashable
        frozen = sorted(list({frozenset(s) for s in groups.values()}), key=len, reverse=True)
        print(len(frozen[0]) * len(frozen[1]) * len(frozen[2]))

    # terrible efficiency, union find would be optimal, might try to implement it later
    new = groups[a].union(groups[b])

    for el in new:
        groups[el] = new

    if len(groups[a]) == len(nodes):
        print(nodes[a][0] * nodes[b][0])
        break
