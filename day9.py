import pprint
pp = pprint.PrettyPrinter(indent=4, width=5000)

# Read the input
f = open("input9.txt", "r")
lines = f.read().splitlines()

#grid = [[99]*10]*10
grid = []
for x, line in enumerate(lines):
    grid.append([int(l) for l in line])




hightSum = 0
for y, line in enumerate(grid):
    for x, height in enumerate(line):
        counter = 0
        #print(grid[y][x])
        if x != 0:
            #check top
            if grid[y][x] < grid[y][x-1]:
                counter += 1
        else:
            counter += 1
        if y != len(grid)-1:
            #check bottom
            if grid[y][x] < grid[y+1][x]:
                counter += 1
        else:
            counter += 1
        if y != 0:
            #check left
            if grid[y][x] < grid[y-1][x]:
                counter += 1
        else:
            counter += 1
        if x != len(line) - 1:
            #check right
            if grid[y][x] < grid[y][x+1]:
                counter += 1
        else:
            counter += 1
        if counter == 4:
            hightSum += grid[y][x] + 1
            #print(grid[y][x], x, y)

print('part1: ', hightSum)

countingIndex = 100
joinedBasins = []
for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if grid[y][x] == 9:
            continue
        counter = 0
        if x != 0:
            if grid[y][x-1] > 9:
                grid[y][x] = grid[y][x-1]
                counter += 1
        if y != len(grid)-1:
            if grid[y+1][x] > 9:
                if grid[y][x] > 9 and grid[y][x] != grid[y+1][x]:
                    lower = min(grid[y][x], grid[y+1][x])
                    higher = max(grid[y][x], grid[y+1][x])
                    joinedBasins.append((lower, higher))
                grid[y][x] = grid[y+1][x]
                counter += 1
        if y != 0:
            if grid[y-1][x] > 9:
                if grid[y][x] > 9 and grid[y][x] != grid[y-1][x]:
                    lower = min(grid[y][x], grid[y-1][x])
                    higher = max(grid[y][x], grid[y-1][x])
                    joinedBasins.append((lower, higher))
                grid[y][x] = grid[y-1][x]
                counter += 1
        if x != len(line) - 1:
            if grid[y][x+1] > 9:
                if grid[y][x] > 9 and grid[y][x] != grid[y][x+1]:
                    lower = min(grid[y][x], grid[y][x+1])
                    higher = max(grid[y][x], grid[y][x+1])
                    joinedBasins.append((lower, higher))
                grid[y][x] = grid[y][x+1]
                counter += 1
        if counter == 0:
            grid[y][x] = countingIndex
            countingIndex += 1
        if counter > 1:
            #pp.pprint(grid)
            continue

for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if height == 9:
            grid[y][x] = 9

basinsDict = {}
'''
for first, second in joinedBasins:
    if first in basinsDict and second in basinsDict[first]:
        continue
    if first in basinsDict:
        basinsDict[first].append(second)
    else:
        for index, value in enumerate(basinsDict.values()):
            if first in value:
                k = list(basinsDict.keys())[index]
                basinsDict[k].append(second)
                break
        else:
            basinsDict[first] = [second]
'''

joinedBasins.sort(key=lambda tup: tup[0])
for first, second in joinedBasins:
    if first in basinsDict and second not in basinsDict:
        basinsDict[second] = basinsDict[first]
        continue
    if first not in basinsDict and second not in basinsDict:
        basinsDict[second] = first
        pass

for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if height in basinsDict:
            grid[y][x] = basinsDict[height]

countBainSizes = {}
for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if height == 9:
            continue
        if height in countBainSizes:
            countBainSizes[height] += 1
        else:
            countBainSizes[height] = 1

print(countBainSizes)

values = list(countBainSizes.values())
countBainSizes = sorted(countBainSizes)
#print('countBainSizes', countBainSizes)

f = max(values)
values.remove(f)
g = max(values)
values.remove(g)
h = max(values)
values.remove(h)
print(f, g, h)
print(f * g * h)


for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if height == 9:
            grid[y][x] = '-'
#pp.pprint(grid)
#print(joinedBasins)
#
#print(basinsDict)



#24015264 too high
#23936640 too high
#768768 not correct
#835380 not correct
#872508 not correct