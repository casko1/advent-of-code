import re

line = open("2.txt").readlines()[0]
numbers = re.findall(r"\d+", line)

p1 = 0
p2 = 0

for i, k in zip(numbers[0::2], numbers[1::2]):
    for s in map(str, range(int(i), int(k) + 1)):
        s_len = len(s)
        if s[:s_len // 2] == s[s_len // 2:]:
            p1 += int(s)
            p2 += int(s)
            continue

        if s in (s + s)[1:-1]:
            p2 += int(s)

print(p1, p2)
