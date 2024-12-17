from itertools import product

with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

def evaluate(numbers, item):
    res = numbers[0]
    for i in range(len(item)):
        if item[i] == '+':
            res += numbers[i+1]
        elif item[i] == '|':
            resStr = str(res) + str(numbers[i+1])
            res = int(resStr)
        else:
            res *= numbers[i+1]
    return res

total = 0
for line in data:
    testValue, numbers = line.strip().split(":")
    testValue = int(testValue)
    numbers = list(map(int, numbers.strip().split()))

    # i need to generate all possible combinations
    for combi in product('+*|', repeat=len(numbers)-1): #('+',), ('*',)
        if evaluate(numbers, combi) == testValue:
            total += testValue
            break
    
print(total)