with open('input.txt', 'r') as file:
    data = file.read().splitlines()

count = 0
for line in data:
    level = list(map(int, line.split())) # need to convert the numbers in list to int 
    sortedLevel = sorted(level)
    sortedDescending = sorted(level, reverse=True)
    if not (level == sortedLevel or level == sortedDescending):
        continue

    isGood = True
    for i in range(len(level)-1):
        diff = int(level[i]) - int(level[i+1])
        if not (1 <= abs(diff) <= 3):
            isGood = False
            break
    if isGood:
        count += 1

print(count)