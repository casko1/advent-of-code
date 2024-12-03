import re

lines = open("3.txt").readlines()


def parse(lst, toggle):
    out = 0
    state = 1
    for line in lst:
        ops = list(re.findall(r"don?\'?t?\(\)|mul\(\d+,\d+\)", line))
        for op in ops:
            if op == "don't()":
                state = 0
            elif op == "do()":
                state = 1
            else:
                n1, n2 = list(map(int, re.findall(r"\d+", op)))
                out += n1 * n2 * (state ** toggle)

    return out


print(parse(lines, 0))
print(parse(lines, 1))
