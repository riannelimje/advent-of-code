from functools import cache

with open('input.txt', 'r') as file:
    data = file.read().strip()

stones = list(map(int,data.split()))

# using part 1 solution to get the get the number of stones after 75 blinks takes too long

# basically to get the number of stones at the bottom most step recursively
# stores the number itself instead of the list of that size 
@cache #decorater function to store prev results
def count(stone,steps):
    # if there are no steps left 
    if steps == 0:
        return 1 # since exactly one stone passed into the function
    if stone == 0:
        return count(1, steps-1) # steps-1 since one fewer step remaining
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length//2]), steps-1) + count(int(string[length//2:]), steps-1)
    return count(stone*2024, steps-1)

sum = 0
for stone in stones:
    sum += count(stone, 75)

print(sum)