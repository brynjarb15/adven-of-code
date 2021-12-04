import pprint
pp = pprint.PrettyPrinter(indent=4)


# read the lines and create a bingo array
def readAndCreateBingoBoard(lines):
    board = []
    for line in lines:
        currentLine = []
        currentLine.append(line[0:2])
        currentLine.append(line[2:5])
        currentLine.append(line[5:8])
        currentLine.append(line[8:11])
        currentLine.append(line[11:14])
        currentLine = [int(l) for l in currentLine]
        board.append(currentLine)
    return board

class BingoBoard:
    #Create bingo board and bingo checker 
    def __init__(self, lines, id):
        self.id = id
        self.board = readAndCreateBingoBoard(lines)
        self.positions = {}
        for x in range(5):
            for y in range(5):
                self.positions[self.board[x][y]] = (x,y)

        self.bingoCheck = {
            "rows" : [0,0,0,0,0],
            "columns": [0,0,0,0,0]
        }

    # Make visual board
    def print(self):
        pp.pprint(self.board)
    
    def updateBoard(self, value):
        # Check if value is on the board
        if value not in self.positions.keys():
            return 0
        # Get x and y coordinates
        x, y = self.positions[value]
        # Put x to make more visual
        self.board[x][y] = 'X'
        # Update bingo checker
        self.bingoCheck["rows"][x] += 1
        self.bingoCheck["columns"][y] += 1
        
        # Check if there is a bingo
        sum = 0
        if self.bingoCheck["rows"][x] == 5 or self.bingoCheck["columns"][y] == 5:
            for a in self.board:
                for b in a:
                    if b != 'X':
                        sum += b
        return sum
        
    
# Read the input
f = open("input4.txt", "r")
lines = f.read().splitlines()

# Get the numbers that will be drawn in the bingo
drawNumbers = lines[0].split(',')
drawNumbers = [int(x) for x in drawNumbers]

# skip first 2 lines
lines = lines[2:]


#create all the bingo boards
i = 0
j = 0
allBingoBoards = []
while i < len(lines):
    a = BingoBoard(lines[i:i+5], j)
    allBingoBoards.append(a)
    i += 6
    j += 1

doneIds = []
print(len(allBingoBoards))
for nextNumber in drawNumbers:
    for board in allBingoBoards:
        if board.id in doneIds:
            #Don't check the completed boards
            continue
        checker = board.updateBoard(nextNumber)
        if checker != 0:
            doneIds.append(board.id)
            #Print out the first board
            if len(doneIds) == 1: 
                board.print()
                print('board id', board.id)
                print('part1: ', checker*nextNumber)
            #Print out the seccond board
            if len(doneIds) == 100:
                board.print()
                print('board id', board.id)
                print('part2: ', checker*nextNumber)
            
            
#6794 is too low            

