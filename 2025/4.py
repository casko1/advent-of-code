import re

lines = open("4.txt").readlines()
directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]


def find_rolls():
    # TIL you can write for comprehensions like this instead of one lining it
    return {
        (m.start(), i)
        for i, line in enumerate(lines)
        for m in re.finditer(r"@", line)
    }


def remove_rolls():
    rolls = find_rolls()

    remove = [0]
    results = []

    while len(remove) != 0:
        results.append(len(remove))
        rolls -= set(remove)
        remove = []

        for rx, ry in rolls:
            if sum((rx + dx, ry + dy) in rolls for dx, dy in directions) < 4:
                remove.append((rx, ry))

    return results[1], sum(results[1:])


p1, p2 = remove_rolls()
print(p1, p2)
