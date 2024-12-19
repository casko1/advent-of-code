from itertools import product
import re

ops = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "c": lambda x, y: int(f"{x}{y}")}
lines = open("7.txt").readlines()
numbers = [list(map(int, re.findall(r"\d+", x))) for x in lines]

op_orders = {}

for i in range(1, 12):
    op_orders[i] = [list(c) for c in product(ops.keys(), repeat=i)]

part1 = 0
part2 = 0

for eq in numbers:
    for comb in op_orders[len(eq) - 2]:
        tmp_sum = 0
        for i in range(1, len(eq) - 1):
            if tmp_sum > eq[0]:
                break

            current_op = comb[i - 1]
            if tmp_sum == 0:
                tmp_sum = ops[current_op](eq[i], eq[i + 1])
            else:
                tmp_sum = ops[current_op](tmp_sum, eq[i + 1])

        if tmp_sum == eq[0]:
            if "c" not in comb:
                part1 += tmp_sum
            part2 += tmp_sum
            break

print(part1)
print(part2)
