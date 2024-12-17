from itertools import combinations

with open('input.txt', 'r') as file:
    data = file.read().splitlines()

grid = list(list(line) for line in data)
n = len(grid)
m = len(grid[0])
antinodes = set()
frequencies = set()
freqDict = {}

def checkBoundaries(row,col):
    return 0 <= row < n and 0 <= col < m
    
def findAllFreq(freq, r, c):
    for i in range(r, n):
        for j in range(c, m):
            if grid[i][j] == freq:
                if freq not in freqDict:
                    freqDict[freq] = set()
                freqDict[freq].add((i,j))
    return freqDict

for i in range(n):
    for j in range(m):
        if grid[i][j].isalnum() and len(grid[i][j]) == 1: # is alphanumeric 
            freq = grid[i][j]
            frequencies.add(freq)
            # find all points with the freq in the grid - store in a dict(?)
            freqDict = findAllFreq(freq, i, j)
            
for f in frequencies:
    # find all the possible combinations for the antinodes
    for (r1,c1), (r2,c2) in combinations(freqDict[f], 2):
        rDiff = r1 - r2
        cDiff = c1 - c2
        if checkBoundaries(r1 + rDiff, c1 + cDiff):
            antinodes.add((r1 + rDiff, c1 + cDiff))
        if checkBoundaries(r2 - rDiff, c2 - cDiff):
            antinodes.add((r2 - rDiff, c2 - cDiff))

print(len(antinodes))