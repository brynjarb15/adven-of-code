

f = open("input1.txt", "r")
numbers = f.read().splitlines()
numbers = [int(n) for n in numbers]






currentNumber = 0
lastNumber = 999999999999999999999999
counter = 0
for n in numbers:
    currentNumber = int(n)
    if lastNumber < currentNumber:
      counter += 1
    lastNumber = currentNumber
print('day1: ' + str(counter))      

first = 0
second = 0
third = 0
sums = []
for index, n in enumerate(numbers):
    if(index + 2 < len(numbers)):
        sums.append(numbers[index] + numbers[index+1] + numbers[index+2])


# same as for day 1
currentNumber = 0
lastNumber = 999999999999999999999999
counter = 0
for n in sums:
    currentNumber = int(n)
    if lastNumber < currentNumber:
      counter += 1
    lastNumber = currentNumber
print('day2: ' + str(counter))    
