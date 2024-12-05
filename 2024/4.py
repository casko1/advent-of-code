from collections import defaultdict

lines = open("4.txt").read().split("\n")
letter_positions = defaultdict(list)
padding = ["." for _ in range(len(lines[0]) + 2)]
m = [padding, padding]

for i, line in enumerate(lines):
    tmp = ["."]
    for j, c in enumerate(list(line)):
        letter_positions[c].append((i, j))
        tmp.append(c)
    tmp.append(".")
    m.insert(len(m) - 1, tmp)


def find(directions, positions, target_word):
    checked_a = defaultdict(lambda: 0)
    total = 0
    for x, y in positions:
        for d in directions:
            found = 1
            tmp_a_pos = None
            for k in range(1, len(target_word)):
                current = m[x + 1 + d[0] * k][y + 1 + d[1] * k]
                if current != target_word[k]:
                    found = 0
                    break
                if target_word[k] == "A":
                    tmp_a_pos = (x + 1 + d[0] * k, y + 1 + d[1] * k)
            if found == 1:
                checked_a[tmp_a_pos] += 1
                total += 1

    return total, len([a for a in checked_a.values() if a == 2])


p1, _ = find([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]], letter_positions["X"], "XMAS")
_, p2 = find([[1, 1], [-1, -1], [1, -1], [-1, 1]], letter_positions["M"], "MAS")

print(p1)
print(p2)
