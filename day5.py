import pprint
pp = pprint.PrettyPrinter(indent=4)

# Read the input
f = open("input5.txt", "r")
lines = f.read().splitlines()


class Hydroline:
    def __init__(self, lines):
        # Flag to check the diagonl lines or not, for part 1 and 2
        checkDiagonalLines = False
        grid = []
        gridSize = 1000
        # Create grid with inital value 0
        for x in range(gridSize):
            nextLine = []
            for y in range(gridSize):
                nextLine.append(0)
            grid.append(nextLine)
        for line in lines:
            # read the lines and get the values
            line = line.split(' -> ')
            first= line[0].split(',')
            last = line[1].split(',')
            x1 = int(first[0])
            y1 = int(first[1])
            x2 = int(last[0])
            y2 = int(last[1])
            # Check diagonal lines
            if x1 - x2 == y1 - y2 and checkDiagonalLines:
                if x1 - x2 < 0:
                    i = x1
                    j = y1
                    while i <= x2:
                        grid[j][i] += 1
                        i += 1
                        j += 1
                elif x1 - x2 > 0:
                    i = x1
                    j = y1
                    while i >= x2:
                        grid[j][i] += 1
                        i -= 1
                        j -= 1
            # Check other diagonal lines
            if -(x1 - x2) == y1 - y2 and checkDiagonalLines:
                i = x1
                j = y1
                # first we do the one way if it is posible
                while i <= x2:
                    grid[j][i] += 1
                    i += 1
                    j -= 1
                
                # Then we do the other way if that is posible
                i = x1
                while i >= x2:
                    grid[j][i] += 1
                    i -= 1
                    j += 1  
            # Check straight lines  
            
            elif x1 == x2:
                i = min(y1, y2)
                end = max(y1, y2)
                while i <= end:
                    grid[i][x1] += 1
                    i += 1
            elif y1 == y2:
                i = min(x1, x2)
                end = max(x1, x2)
                while i <= end:
                    grid[y1][i] += 1
                    i += 1
        #Count where it is 2 or higher
        counter = 0
        for line in grid:
            for value in line:
                if value > 1:
                    counter += 1
        print(counter)


            
        
a = Hydroline(lines)

