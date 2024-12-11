with open('input.txt', 'r') as file:
    data = file.read().splitlines()

def isSafe(level):
    sortedLevel = sorted(level)
    sortedDescending = sorted(level, reverse=True)
    if not (level == sortedLevel or level == sortedDescending):
        return False
    for i in range(len(level)-1):
        diff = int(level[i]) - int(level[i+1])
        if not (1 <= abs(diff) <= 3):
            return False
    return True
     
count = 0
for line in data:
    level = list(map(int, line.split())) # need to convert the numbers in list to int 
    
    if isSafe(level):
        count +=1 
        continue

    isGood = False
    for i in range(len(level)):
        temp = level[:i] + level[i+1:] # remove 1 element until is safe
        if isSafe(temp):
            isGood = True
            break

    if isGood:
        count += 1

print(count)