import pprint
import copy
pp = pprint.PrettyPrinter(indent=4, width=500)

# Read the input
f = open("input14.txt", "r")
lines = f.read().splitlines()


input = lines[0]

rulesList = lines[2:]
rules = {}
for rule in rulesList:
    r = rule.split(' -> ')
    rules[r[0]] = r[1]
first = input

for i in range(10):
    newString = ''
    newLetters = ''
    lastLetter = first[:1]
    for letter in first[1:]:
        pair = lastLetter + letter
        between = rules[pair]
        newLetters = newLetters + between
        newString = newString + lastLetter + between
        lastLetter = letter
    newString += first[-1:]
    first = newString

allLetters = ''.join(set(newString))
min = 9999999999999
max = 0
countLetters = {}
for letter in allLetters:
    count = newString.count(letter)
    countLetters[letter] = count
    if count < min:
        min = count
    if count > max:
        max = count
print('Part 1:', max-min)

pairs = {}
first = input
lastLetter = first[:1]
for letter in first[1:]:
    pair = lastLetter + letter
    pairs[pair] = 1
    lastLetter = letter

for i in range(40):
    oldParis = copy.deepcopy(pairs)
    for pair in oldParis.keys():
        amount = oldParis[pair]
        a = pair[0] + rules[pair]
        b = rules[pair] + pair[1]
        if a in pairs:
            pairs[a] += amount
        else:
            pairs[a] = amount
        if b in pairs:
            pairs[b] += amount
        else:
            pairs[b] = amount
        pairs[pair] -= amount

letterCount = {}

for index, pair in enumerate(pairs.keys()):
    if pair[0] in letterCount:
        letterCount[pair[0]] += pairs[pair]
    else:
        letterCount[pair[0]] = pairs[pair]
letterCount[input[-1]] += 1
        
    


min = 9999999999999
max = 0
for l in letterCount:
    c = letterCount[l]
    if c < min:
        min = c
    if c > max:
        max = c
print('Part 2:', max-min)


