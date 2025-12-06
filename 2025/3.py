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

    return int("".join(stack[:n]))


p1 = sum(find_max(line, 2) for line in lines)
p2 = sum(find_max(line, 12) for line in lines)

print(p1, p2)
