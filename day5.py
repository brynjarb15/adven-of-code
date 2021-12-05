import pprint
pp = pprint.PrettyPrinter(indent=4)

# Read the input
f = open("input5.txt", "r")
lines = f.read().splitlines()
#pp.pprint(lines)


class Hydroline:
    def __init__(self, lines):
        grid = []
        for x in range(10):
            nextLine = []
            for y in range(10):
                nextLine.append(0)
            grid.append(nextLine)
        lines = ['0,1 -> 3,4']
        for line in lines:
            line = line.split(' -> ')
            first= line[0].split(',')
            last = line[1].split(',')
            x1 = int(first[0])
            y1 = int(first[1])
            x2 = int(last[0])
            y2 = int(last[1])
            print(x1, y1, x2, y2)
            if (x1 == y2 and x2 == y2) or (x1 == y1 and x2 == y2):
                if x1 - x2 == y1 - y2:
                    if x1 - x2 < 0:
                        i = x1
                        j = y1
                        while i <= x2:
                            grid[j][i] += 1
                            i += 1
                            j += 1
                    elif x1-x2 > 0:
                        i = x1
                        j = y1
                        while i <= x2:
                            grid[j][i] += 1
                            i -= 1
                            j -= 1

                '''
                if x1 < x2:
                    if y1 < y2:
                        print('here2')
                        i = x1
                        j = y1
                        while i <= x2:
                            grid[j][i] += 1
                            i += 1
                            j += 1
                    if y1 > y2:
                        print('here1')
                        i = x1
                        j = y1
                        while i <= x2:
                            grid[j][i] += 1
                            i += 1
                            j -= 1
                elif x1 > x2:
                    if y1 < y2:
                        i = x1
                        j = y1
                        while i >= x2:
                            grid[j][i] += 1
                            i -= 1
                            j -= 1
                    if y1 > y2:
                        pass
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
            '''
        pp.pprint(grid)
        counter = 0
        for line in grid:
            for value in line:
                if value > 1:
                    counter += 1
        print(counter)


            
        
a = Hydroline(lines)

