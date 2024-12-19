with open('test.txt', 'r') as file:
    data = file.read().strip()

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

# store a tuple (start, end) - [inclusive, exclusive) for the consecutive . 
dots = []
start = 0
end = 0
for i in range(len(arr)):
    if arr[i] == '.':
        start = i
        for j in range(i, len(arr)):
            if arr[j] != '.':
                end = j
                break
        if dots == []:
            dots.append((start, end))
            continue
        if start < dots[-1][-1]:
            continue
        dots.append((start, end))
print("dots are")
print(dots)
print("--------")
print("original arr")
print(arr)
print("--------")

# find the length of the dots 
def dotLen(length):
    for start, end in dots:
        dotLen = end - start + 1
        if dotLen > length:
            return start, end 
    return 0,0

# print(dots)
dictionary = {}
length = 0
# get the length of all the numbers put in a dictionary maybe 
for i in range(len(arr)-1, -1, -1):
    if arr[i] != '.':
        num = arr[i]
        if num not in dictionary:
            dictionary[num] = 1 
        if num == arr[i-1]:
            dictionary[num] += 1


# find the corresponding dots to the length 
for key, value in dictionary.items():
    if dotLen(value) != (0,0):
        # print(value)
        # print(dotLen(value))
        # print("went in")
        start, end = dotLen(value)
        dots.remove((start,end))
        # have to also add back the dots if it is not being used
        if end >= start + value:
            dots.insert(0, (start+value, end))
        # print(dots)
        # print(start)
        # print(end)
        arr[start:start+value] = [key] * value
        print(arr)
        
        # need to also find a way to delete the elements that are swapped

print(dictionary)