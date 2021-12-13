import pprint
pp = pprint.PrettyPrinter(indent=4, width=5000)

# Read the input
f = open("input10.txt", "r")
lines = f.read().splitlines()

openCharacters = '([{<'
closeCharacters = ')]}>'
incorrectChars = ''
beginning = ''
incompleteScores = []
for line in lines:
    beginning = ''
    corrupted = False
    for s in line:
        if s in openCharacters:
            beginning = beginning + s
        elif s in closeCharacters:
            lastCharacter = beginning[-1:]
            # Check if the next one and the last one make a pair and then we remove them
            if closeCharacters.index(s) == openCharacters.index(lastCharacter):
                beginning = beginning[:-1]
            else:
                # We get closing that not corresponds to the last opening so we mark it as corrupted and add it to 
                corrupted = True
                incorrectChars = incorrectChars + s
                break
    score = 0
    if not corrupted:
        # Go through beginning in reverse because we are looking at the close sequence
        for s in beginning[::-1]:
            score = score * 5
            score = score + openCharacters.index(s) + 1
        incompleteScores.append(score)


a = incorrectChars.count(')')
b = incorrectChars.count(']')
c = incorrectChars.count('}')
d = incorrectChars.count('>')
print('Part 1: ', a*3 + b*57 + c*1197 + d*25137)


# Find the score in the middle and print it out
incompleteScores.sort()
print('Part 2: ', incompleteScores[int(len(incompleteScores)/2)])




