with open('input.txt', 'r') as file:
    data = file.read().splitlines()

list1 = []
list2 = []

for line in data:
    x,y = line.split()
    list1.append(int(x))
    list2.append(int(y))

list1.sort()
list2.sort()

distance = 0

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i]) 

print(distance)
