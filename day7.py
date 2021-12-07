import pprint
pp = pprint.PrettyPrinter(indent=4)

# Read the input
f = open("input7.txt", "r")
lines = f.read()
positions = lines.split(',')
positions = [int(p) for p in positions]
pp.pprint(max(positions))
print(len(positions))

#1000 numbers
#min = 0
#max = 1946
minDist = 9999999999999
minFuel = 9999999999999
i = 0
part1 = False
while i <= max(positions):
    currentDist = 0
    currentFuel = 0
    for pos in positions:
        distFromPos = abs(i - pos)
        if part1:
            currentDist += distFromPos
        else: #part 2
            currentFuel += (distFromPos * (distFromPos+1))/2
        
    if currentDist < minDist:
        minDist = currentDist
    if currentFuel < minFuel:
        minFuel = currentFuel
    i += 1
print('part 1: ', minDist)
print('part 2: ', minFuel)
