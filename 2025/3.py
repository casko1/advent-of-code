import re

lines = open("3.txt").readlines()


def find_max(number, n):
    nums = list(re.findall(r"\d", number))

    drop = len(nums) - n
    stack = []

    for d in nums:
        while drop > 0 and len(stack) > 0 and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)

    stack = stack[:n]

    return int("".join(stack))


p1 = 0
p2 = 0

for line in lines:
    p1 += find_max(line, 2)
    p2 += find_max(line, 12)

print(p1, p2)
