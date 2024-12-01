from collections import Counter

lines = open("1.txt").readlines()
left, right = zip(*(map(int, line.split()) for line in lines))

left = sorted(left)
right = sorted(right)

part1 = sum(abs(left[i] - right[i]) for i in range(len(left)))

print(part1)

c = Counter(right)

part2 = sum(x * c[x] for x in left)

print(part2)
