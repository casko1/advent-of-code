lines = open("1.txt").readlines()

operation = {"R": lambda x: x + 1, "L": lambda x: x - 1}
current = 50
p1 = p2 = 0

for line in lines:
    op, n = line[:1], int(line[1:])
    for _ in range(n):
        current = operation[op](current)

        if current % 100 == 0:
            p2 += 1

    if current % 100 == 0:
        p1 += 1

print(p1, p2)
