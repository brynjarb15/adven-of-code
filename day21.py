
playerOne = 9
playerTwo = 3



def playTurn(pos, i):
    if i == 99:
        pos += 99 + 100 + 1
    if i == 100:
        pos += 100 + 1 + 2
    else:
        pos += i*3 + 3
    pos = pos%10
    if pos == 0:
        pos = 10
    return pos
    
playerOneScore = 0
playerTwoScore = 0
playerOneTurn = True
i = 1
counter = 0
while playerOneScore < 1000 and playerTwoScore < 1000:
    counter += 3
    if playerOneTurn:
        playerOne = playTurn(playerOne, i)
        playerOneScore += playerOne
    else:
        playerTwo = playTurn(playerTwo, i)
        playerTwoScore += playerTwo
    if playerOneTurn:
        print(1, i, playerOne, playerOneScore)
    else:
        print(2, i, playerTwo, playerTwoScore)
    playerOneTurn = not playerOneTurn
    i += 3
    i = i%100
    if i == 0:
        i = 100
print('Part 1:', min(playerOneScore, playerTwoScore)*counter)
