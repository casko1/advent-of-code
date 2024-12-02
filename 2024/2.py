from itertools import combinations

lines = open("2.txt").readlines()
reports = [list(map(int, line.split())) for line in lines]


def generate_subsequences(lst):
    return [list(combo) for combo in combinations(lst, len(lst) - 1)]


def classify_report(report):
    previous = None
    for a, b in zip(report, report[1:]):
        diff = a - b
        if abs(diff) > 3 or diff == 0:
            return 0
        elif previous is None or previous * diff > 0:
            previous = diff
        else:
            return 0

    return 1


part1 = sum(classify_report(r) for r in reports)

print(part1)

part2 = 0

for r in reports:
    combs = generate_subsequences(r)
    part2 += 1 if any(classify_report(c) for c in combs) else 0

print(part2)
