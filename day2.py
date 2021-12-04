

f = open("input2.txt", "r")
commands = f.read().splitlines()


dict = {}
for c in commands:
    a = c.split(' ')
    if a[0] in dict:
        dict[a[0]] += int(a[1])
    else:
        dict[a[0]] = int(a[1])




x = dict['forward']
y = dict['down'] - dict['up']
print('part1: ' + str(x*y))





aim = 0
forward = 0
depth = 0
for c in commands:
    c = c.split(' ')
    command = c[0]
    value = int(c[1])
    if command == 'forward':
        forward += value
        depth += value*aim
    if command == 'down':
        aim += value
    if command == 'up':
        aim -= value


print('part2: ' + str(depth*forward))