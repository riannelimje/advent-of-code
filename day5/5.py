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
        # for the following numbers ensure it does not appear in the list of numbers that should come before
        for nextNum in update[idx+1:]:
            if num in ruleDict and nextNum in ruleDict[num]:
               return False
    return True

sum = 0
for update in updates:
    update = update.split(",")
    if isCorrect(update):
        middlePage = len(update) // 2
        sum += int(update[middlePage])
        
print(sum)