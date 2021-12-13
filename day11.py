import pprint
pp = pprint.PrettyPrinter(indent=4, width=50)

# Read the input
f = open("input11.txt", "r")
lines = f.read().splitlines()





grid = []
# Create grid
for line in lines:
    nextLine = []
    for spot in line:
        nextLine.append(int(spot))
    grid.append(nextLine)


  
def addOneToGridPos(x, y):
    try:
        grid[x][y] += 1
    except IndexError:
        pass

def printGrid():
    for line in grid:
        a = [str(l) for l in line]
        print(''.join(a))
        #for spot in line:

totalFlashCounter = 0
for i in range(1000):
    currentFlashCounter = 0
    sombodyFlashed = True
    allreadyFlashed = []

    # Increase all by 1
    for x, line in enumerate(grid):
        for y, spot in enumerate(line):
            grid[x][y] += 1
            
    # Check if sombody flashed 
    while sombodyFlashed:
        sombodyFlashed = False
        for x, line in enumerate(grid):
            for y, spot in enumerate(line):
                if spot >= 10:
                    if (x,y) not in allreadyFlashed:
                        currentFlashCounter += 1
                        totalFlashCounter += 1
                        sombodyFlashed = True
                        allreadyFlashed.append((x,y))
                        addOneToGridPos(x+1, y)
                        addOneToGridPos(x, y+1)
                        addOneToGridPos(x+1, y+1)
                        if x != 0:
                            addOneToGridPos(x-1, y)
                            addOneToGridPos(x-1, y+1)
                        if y != 0:
                            addOneToGridPos(x, y-1)
                            addOneToGridPos(x+1, y-1)
                        if x != 0 and y != 0:
                            addOneToGridPos(x-1, y-1)

    #Update all that flashed back to 0
    for x, line in enumerate(grid):
        for y, spot in enumerate(line):
            if spot >= 10:
                grid[x][y] = 0
    if i == 100-1:
        print('Part 1: ' + str(totalFlashCounter))
    if currentFlashCounter == 100:
        print('Part 2: ' + str(i + 1))
        break          