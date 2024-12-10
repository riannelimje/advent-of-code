with open('input.txt', 'r') as file:
    data = file.read().splitlines()

list1 = []
list2 = []

for line in data:
    x,y = line.split()
    list1.append(int(x))
    list2.append(int(y))

set1 = set(list1)
dict = {}

for i in range(len(list2)):
    if list2[i] in set1:
        dict[list2[i]] = dict.get(list2[i],0) + 1

similarity = 0

for i in range(len(list1)):
    similarity += dict.get(list1[i],0) * list1[i]

print(similarity)
