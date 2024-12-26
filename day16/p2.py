import heapq # heap is a priority queue
from collections import deque

with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

grid = list(list(line) for line in data)

n = len(grid)
m = len(grid[0])

def findStart():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                return i,j

sr, sc = findStart()

# dijkstra's algorithm 
pq = [(0,sr,sc,0,1,None,None,None,None)] # cost, start coordinates and direction, the Nones are the prev ones
lowestCost = {(sr,sc,0,1): 0}
backtrack = {} # foreach position, all of the previous states along the path 
bestCost = float("inf") # lowest cost to get to the end 
endStates = set() # list of all possible states to get to the end 

while pq:
    cost, r, c, dr, dc, lr, lc, ldr, ldc = heapq.heappop(pq) # next available cheapest option to look at 
    if cost > lowestCost.get((r,c,dr,dc), float("inf")):
        continue
    lowestCost[(r,c,dr,dc)] = cost
    if grid[r][c] == 'E': 
        if cost > bestCost:
            break 
        bestCost = cost
        endStates.add((r,c,dr,dc))
    if (r,c,dr,dc) not in backtrack:
        backtrack[(r,c,dr,dc)] = set()
    backtrack[(r,c,dr,dc)].add((lr,lc,ldr,ldc))
    # for each of the new states
    for newCost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == '#':
            continue
        if cost > lowestCost.get((nr, nc, ndr, ndc), float("inf")):
            continue
        heapq.heappush(pq, (newCost, nr, nc, ndr, ndc, r, c, dr, dc))

# fill out the backtrack 
states = deque(endStates) # initialise a queue with end states 
seen = set(endStates) # mark end states as seen

while states:
    key = states.popleft()
    for last in backtrack.get(key, []): # need the [] since the first one is None - NoneType object is not iterable
        if last in seen:
            continue
        if None in last: # remove the nonexistent None
            continue
        seen.add(last)
        states.append(last)

tiles = set() # remove duplicates 
for r, c, _, _ in seen:
    tiles.add((r,c))

print(len(tiles)) 