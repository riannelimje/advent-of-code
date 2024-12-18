with open('input.txt', 'r') as file:
    data = file.read().strip()

# even will be the files
# odd will be the free space
arr = []
index = 0

for i in range(len(data)):
    if i%2==0:
        for i in range(int(data[i])):
            arr.append(index)
        index +=1
    else:
        for i in range(int(data[i])):
            arr.append('.')

i = 0
while i < len(arr):
    if arr[i] == '.':
        ele = arr.pop()
        while ele == '.':
            ele = arr.pop()
        arr[i] = ele
    i += 1

sum = 0 
idx = 0
for num in arr:
    sum += num * idx
    idx +=1

print(sum)