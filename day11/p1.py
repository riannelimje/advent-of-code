with open('input.txt', 'r') as file:
    data = file.read().strip()

stones = list(data.split(' '))

def removeLeadingZeros(num):
    for i in range(len(num)):
        if num[i] != '0':
            res = num[i::] #return the remaining string
            return res
    return '0'

def change(stones):
    changed = []
    for i, value in enumerate(stones):
        if value == '0':
            changed.append('1')
        elif len(value) % 2 == 0:
            half = len(value) // 2 
            changed.append(removeLeadingZeros(value[:half]))
            changed.append(removeLeadingZeros(value[half:]))
        else:
            newValue = int(value) * 2024
            changed.append(str(newValue))
    return changed

for i in range(25):
    stones = change(stones)

print(len(stones))