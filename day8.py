import pprint
pp = pprint.PrettyPrinter(indent=4)

# Read the input
f = open("input8.txt", "r")
lines = f.read().splitlines()
outputs = [l.split(' | ')[1] for l in lines]
inputs = [l.split(' | ')[0] for l in lines]

def print7Segment(segments):
    print(' ' + segments['top']*4)
    print(segments['L1'] + ' '*4 + segments['R1'])
    print(segments['L1'] + ' '*4 + segments['R1'])
    print(' ' + segments['middle']*4)
    print(segments['L2'] + ' '*4 + segments['R2'])
    print(segments['L2'] + ' '*4 + segments['R2'])
    print(' ' + segments['bottom']*4)


def sortString(string):
    return ''.join(sorted(string))

def removeLetters(string, letters):
    for l in letters:
        string = string.replace(l, '')
    return string



segmentTest = {
    'top': 'a',
    'middle': 'b',
    'bottom': 'c',
    'L1': 'd',
    'L2': 'e',
    'R1': 'f',
    'R2': 'g'
}

emptySegment = {
    'top': '',
    'middle': '',
    'bottom': '',
    'L1': '',
    'L2': '',
    'R1': '',
    'R2': ''
}


def solvePart2(inputs, outputs):
    numbers = inputs.split(' ')
    outputs = outputs.split(' ')
    numbers = [sortString(n) for n in numbers]
    outputs = [sortString(o) for o in outputs]
    segments = {
        'top': '',
        'middle': '',
        'bottom': '',
        'L1': '',
        'L2': '',
        'R1': '',
        'R2': ''
    }
    knownNumbers = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
    }
    knownNumbers[1] = [x for x in numbers if len(x) == 2][0]
    knownNumbers[4] = [x for x in numbers if len(x) == 4][0]
    knownNumbers[7] = [x for x in numbers if len(x) == 3][0]
    knownNumbers[8] = [x for x in numbers if len(x) == 7][0]

    # Find top
    seven = knownNumbers[7]
    for letter in knownNumbers[1]:
        seven = seven.replace(letter, '')
    segments['top'] = seven[0]

    # Find bottom, L2, 2, 3 and 5
    lengthOfFive = [x for x in numbers if len(x) == 5]
    newLengthOfFive = []
    shortNumberTwo = ''
    for n in lengthOfFive:
        newLengthOfFive.append(removeLetters(n, knownNumbers[7]))
    shortThree = [x for x in newLengthOfFive if len(x) == 2][0]
    three = lengthOfFive[newLengthOfFive.index(shortThree)]
    knownNumbers[3] = three

    segments['bottom'] = removeLetters(knownNumbers[3], knownNumbers[4] + segments['top'])
    
    segments['L1'] = removeLetters(knownNumbers[4], knownNumbers[3])
    
    for n in lengthOfFive:
        if segments['L1'] in n:
            knownNumbers[5] = n
    segments['middle'] = removeLetters(knownNumbers[3], knownNumbers[1] + segments['bottom'] + segments['top'])

    segments['R2'] = removeLetters(knownNumbers[5], segments['top'] + segments['middle'] + segments['bottom'] + segments['L1'])
    
    lengthOfFive.remove(knownNumbers[3])
    lengthOfFive.remove(knownNumbers[5])
    knownNumbers[2] = lengthOfFive[0]

    segments['L2'] = removeLetters(knownNumbers[2], knownNumbers[7] + segments['middle'] + segments['bottom'])
    unsortedSix = segments['top'] + segments['middle'] + segments['bottom'] + segments['L1'] + segments['L2'] + segments['R2']
    knownNumbers[6] = sortString(unsortedSix)

    segments['R1'] = removeLetters(knownNumbers[8], knownNumbers[6])

    knownNumbers[9] = removeLetters(knownNumbers[8], segments['L2'])
    knownNumbers[0] = removeLetters(knownNumbers[8], segments['middle'])

    keys = list(knownNumbers.keys())
    values = list(knownNumbers.values())
    number = ''
    for output in outputs:
        a = values.index(output)
        number = number + str(a)
    number = int(number)  
        

    #print7Segment(segments)
    #pp.pprint(knownNumbers)
    return number

counter = 0
for output in outputs:
    numbers = output.split(' ')
    for n in numbers:
        length = len(n)
        if length == 2 or length == 4 or length == 3 or length == 7:
            counter += 1

print('print 1: ', counter)

sum = 0
for input, output in zip(inputs, outputs):
    sum += solvePart2(input, output)
print('part 2: ', sum)

