from itertools import combinations

interval_strings, ingredients = open("5.txt").read().split("\n\n")
ingredients = list(map(int, ingredients.split("\n")))
intervals = []

for interval in interval_strings.split("\n"):
    left, right = interval.split("-")
    intervals.append((int(left), int(right)))

while True:
    # very expensive but input is forgiving (this time)
    combs = list(combinations(intervals, 2))
    for (l1, r1), (l2, r2) in combs:
        if r1 < l2 or r2 < l1:
            continue

        intervals.remove((l2, r2))
        intervals.remove((l1, r1))
        intervals.append((min(l1, l2), max(r1, r2)))
        break
    else:
        break

p1 = sum(any(left <= n <= right for left, right in intervals) for n in ingredients)
p2 = sum(right - left + 1 for left, right in intervals)
print(p1, p2)
