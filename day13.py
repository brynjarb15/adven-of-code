import pprint
pp = pprint.PrettyPrinter(indent=4, width=500)

# Read the input
f = open("input13.txt", "r")
lines = f.read().splitlines()

# Print the grid in the same format as on the webiste
def printGrid():
    for line in grid:
        a = [str(l) for l in line]
        print(''.join(a))
        

# Get the dots and folds, the dots come first then empty line and then the folds
dots = []
folds = []
dotsDone = False
for line in lines:
    if line == '':
        dotsDone = True
        continue
    if dotsDone:
        folds.append(line)
    else:
        dots.append(line)

# Parse the fold instructions
folds = [f.replace('fold along ' ,'').split('=') for f in folds]

# Get all the coordinates
coordinates = []
for dot in dots:
    c = dot.split(',')
    c = [int(k) for k in c]
    c = (c[0], c[1])
    coordinates.append(c)

# Make inital sizes that are large enough, it will be cut down to nice size on the first fold
xSize = 1500
ySize = 1500
# Initalize the grid
grid = []
# Create an empty grid
for _ in range(ySize):
    nextLine = []
    for _ in range(xSize):
        nextLine.append('.')
    grid.append(nextLine)


# Put # into the grid on the correct coordinates
for x, y in coordinates:
    grid[y][x] = '#'

#printGrid()
firstFold = True
for fold in folds:
    foldLine = int(fold[1])
    # Make a fold over the y line
    if fold[0] == 'y':
        for y, line in enumerate(grid):
            for x, spot in enumerate(line):
                # Skip all the lines above the fold line
                if y <= foldLine:
                    continue
                # Add the current spot above the line in the correct spot
                if spot == '#':
                    newY = foldLine - (y - foldLine)
                    grid[newY][x] = '#'
        # Cut the lines below the fold line
        grid = grid[:foldLine]
    # Make a fold over the x line
    elif fold[0] == 'x':
        for y, line in enumerate(grid):
            for x, spot in enumerate(line):
                # Skip the lines left of the fold line
                if x <= foldLine:
                    continue
                # Add the dots right of the line to the left of the line
                if spot == '#':
                    newX = foldLine - (x - foldLine)
                    grid[y][newX] = '#'
        # Cut out the lines right of the fold line
        for y, line in enumerate(grid):
            grid[y] = line[:foldLine]
    # Count number of # after the first fold for part 1
    if firstFold:
        firstFold = False
        counter = 0
        for y, line in enumerate(grid):
            for x, spot in enumerate(line):
                if spot == '#':
                    counter += 1


print('Part 1:', counter)
print('Part 2:')
printGrid()