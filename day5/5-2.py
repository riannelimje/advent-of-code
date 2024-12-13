with open("input.txt", "r") as file:
    orderRules, updates = file.read().split("\n\n")
    orderRules = orderRules.splitlines()
    updates = updates.splitlines()

# key: page number, value: list of page numbers that should come before 
ruleDict = {}

for line in orderRules:
    x,y = line.split("|")
    if y not in ruleDict:
        ruleDict[y] = []
    ruleDict[y].append(x)

def isCorrect(update):
    for idx, num in enumerate(update):
        # check for the following numbers - appear in the list of numbers that should come before?
        for nextNum in update[idx+1:]:
            if num in ruleDict and nextNum in ruleDict[num]:
               return False
    return True

# using bubble sort - repeatedly swapping adjacent elements if they are in the wrong order 
def sortCorrectly(update):
    for i in range(len(update)):
        for j in range(len(update)-i-1):
            # check if it's out of order 
            if update[j+1] in ruleDict.get(update[j], []): # return [] if update[j] not found in ruleDict (_ in None will cause error)
                # swap 
                update[j], update[j+1] = update[j+1], update[j]
    return update

sum = 0
for update in updates:
    update = update.split(",")
    if not isCorrect(update):
        # what i need to do now is to order them correctly 
        update = sortCorrectly(update)
        middlePage = len(update) // 2
        sum += int(update[middlePage])
        
print(sum)