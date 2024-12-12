import re

with open("input.txt", "r") as file:
    data = file.read()

def mul(x,y):
    return int(x) * int(y)

# pattern for mul(x,y)
regex = r"mul\(\d+\,\d+\)"

match = re.findall(regex, data) # eg. ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

sum = 0

for ele in match:
   num = ele[4:-1].split(",")
   x = num[0]
   y = num[1]
   sum += mul(x,y)

print(sum)