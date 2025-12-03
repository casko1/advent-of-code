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

        for j in range(1, s_len // 2 + 1):
            if s_len % j == 0:
                chunks = [s[i:i + j] for i in range(0, s_len, j)]
                if all(x == chunks[0] for x in chunks):
                    p2 += int(s)
                    break

print(p1, p2)
