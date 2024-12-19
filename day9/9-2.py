with open('input.txt', 'r') as file:
    data = file.read().strip()

dictionary = {} # store the postion and the length of the number 
blanks = [] # store position of each blanks
pos = 0
fid = 0

for i, char in enumerate(data):
    length = int(char)
    if i % 2 == 0:
        dictionary[fid] = (pos,length)
        fid += 1
    else:
       if length != 0:
            blanks.append((pos,length))

    pos += length


#curr fid will be at the highest one
while fid > 0:
    fid -= 1 # need to account for the fid+1 at line 14 and decrement it each time 
    pos, length  = dictionary[fid]
    for i, (start, bLen) in enumerate(blanks):
        # if the dot goes pass the position of the fid - means it doesn't apply to it anymore
        if start >= pos:
            break
        if length <= bLen:
            dictionary[fid] = (start, length) #replace with the new one
            if length == bLen:
                blanks.pop(i) # delete the whole tuple
            else:
                blanks[i] = (start+length,bLen-length) # replace with the new dot locations 
            break

sum = 0
for fid, (pos,length) in dictionary.items():
    for i in range(pos, pos+length):
        sum += fid * i

print(sum)