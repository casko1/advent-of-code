lines = open('in.txt').read().split('\n')

nums = []

for line in lines:
    dec = 0
    pos = 0
    for ch in reversed(list(line)):
        if ch == '-':
            dec += -1 * (5**pos)
        elif ch == '=':
            dec += -2 * (5**pos)
        else:
            dec += int(ch) * (5**pos)

        pos += 1

    nums.append(dec)

s = sum(nums)
out = ''

# remainder of 4 -> -1 (-), 3 -> -2 (=)
while s > 0:
    r = s % 5
    if r == 4:
        out += '-'
        s += 1
    elif r == 3:
        out += '='
        s += 2
    else:
        out += str(r)

    s //= 5

print(out[::-1])