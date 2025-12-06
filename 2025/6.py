import re

lines = open("6.txt").readlines()

op = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}
operations = re.findall(r"[*+]", lines[-1])


def calculate(groups):
    out = 0
    for k, group in enumerate(groups):
        tmp = 0 if operations[k] == "+" else 1
        for n in group:
            tmp = op[operations[k]](tmp, int(n))

        out += tmp

    return out


number_matrix = []

for line in lines[:-1]:
    number_matrix.append(re.findall(r"\d+", line))

character_matrix = []
for line in lines[:-1]:
    character_matrix.append([x for x in line])

number_groups = []
current_number_group = []

for i in range(len(character_matrix[0])):
    number = ""
    for j in range(len(character_matrix)):
        if "0" <= character_matrix[j][i] <= "9":
            number += character_matrix[j][i]

    if number == "":
        number_groups.append(current_number_group)
        current_number_group = []
    else:
        current_number_group.append(int(number))

p1 = calculate(zip(*number_matrix))
p2 = calculate(number_groups)

print(p1, p2)
