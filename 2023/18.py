import re

lines = open("inputs/18.txt").read().split("\n")
pattern = re.compile(r"\w+")
for line in lines:
    m = re.findall(pattern, line)
    print()
