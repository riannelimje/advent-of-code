import re

with open("input.txt", "r") as file:
    data = file.read()

def mul(x,y):
    return int(x) * int(y)

def findMatch(arr):
    regex = r"mul\(\d+\,\d+\)"
    match = re.findall(regex, arr) # all enabled in beginning
    sum = 0

    for ele in match:
        num = ele[4:-1].split(",")
        x = num[0]
        y = num[1]
        sum += mul(x,y)
    return sum

dontArr = data.split("don't")

total = 0

total += findMatch(dontArr[0])

print(f"total at the start is {total}")

for i in range(1, len(dontArr)):
    arr = dontArr[i].split("do")
    # there might be no do 
    if len(arr) > 1:
        # there might be more than 1 do
        for i in range(1, len(arr)):
            doArr = arr[i]
            total += findMatch(doArr)

print(total)