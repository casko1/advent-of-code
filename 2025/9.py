import re
from itertools import combinations

lines = open("9.txt").readlines()


def area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


points = [(int(a), int(b)) for line in lines for a, b in re.findall(r"(\d+),(\d+)", line)]
edges = [(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]
squares = [((x1, y1), (x2, y2), area(x1, y1, x2, y2)) for (x1, y1), (x2, y2) in combinations(points, 2)]

max_area = max(squares, key=lambda t: t[2])
print(max_area[2])

max_area = 0
for (x1, y1), (x2, y2), a in squares:
    if all(
            min(ey1, ey2) >= max(y1, y2)
            or min(ex1, ex2) >= max(x1, x2)
            or max(ey1, ey2) <= min(y1, y2)
            or max(ex1, ex2) <= min(x1, x2)
            for (ex1, ey1), (ex2, ey2) in edges
    ):
        max_area = max(max_area, a)

print(max_area)
