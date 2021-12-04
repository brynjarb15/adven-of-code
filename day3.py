

f = open("input3.txt", "r")
lines = f.read().splitlines()

#lines = lines[:10]


dict = {
    0: 0, 
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0}
for line in lines:
    for index, bit in enumerate(line):
        if bit == '0':
            dict[index] -= 1
        if bit == '1':
            dict[index] += 1

gamma = ''
epsilon = ''
for d in dict.values():
    if d < 0:
        gamma += '0'
        epsilon += '1'
    elif d > 0:
        gamma += '1'
        epsilon += '0'

print('Part1: ', int(gamma, 2) * int(epsilon, 2))

def countBits(lines, index):
    counter = 0
    for l in lines:
        if l[index] == '1':
            counter += 1
        if l[index] == '0':
            counter -= 1
    return counter
            
currentLines = lines



for index, _ in enumerate(lines[0]):
    #print('start', currentLines)
    if len(currentLines) == 1:
        print(currentLines)
        break
    a = countBits(currentLines, index)
    if a < 0:
        currentLines = [l for l in currentLines if l[index] == '0']
    if a > 0:
        currentLines = [l for l in currentLines if l[index] == '1']
    if a == 0:
        currentLines = [l for l in currentLines if l[index] == '1']
oxygen = currentLines[0]

currentLines = lines

for index, _ in enumerate(lines[0]):
    #print('start', currentLines)
    if len(currentLines) == 1:
        print(currentLines)
        break
    a = countBits(currentLines, index)
    if a < 0:
        currentLines = [l for l in currentLines if l[index] == '1']
    if a > 0:
        currentLines = [l for l in currentLines if l[index] == '0']
    if a == 0:
        currentLines = [l for l in currentLines if l[index] == '0']
co2 = currentLines[0]

print('oxygen', oxygen)
print('co2', co2)
#110111110101
#110111110101 = 3573
#000100100001
#000100100001 = 289

#1032597
#1022193 to low


