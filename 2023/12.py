lines = open("inputs/12.txt").read().split("\n")

templates = []
arrangements = []

for line in lines:
    spl = line.split(" ")
    templates.append(spl[0])
    arrangements.append([int(x) for x in spl[1].split(",")])


def find_arrangements(template, arrangement):
    











total = 0
for t,a in zip(templates, arrangements):
    total += find_arrangements(t, a)