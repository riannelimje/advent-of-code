import heapq # heap is a priority queue

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
pq = [(0,sr,sc,0,1)] # cost, start coordinates and direction
seen = set((sr,sc,0,1))

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq) # next available cheapest option to look at 
    seen.add((r,c,dr,dc))
    if grid[r][c] == 'E': # found the cheapest way to exit 
        print(cost)
        break 
    # for each of the new states
    for newCost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == '#':
            continue
        if (nr, nc, ndr, ndc) in seen:
            continue
        heapq.heappush(pq, (newCost, nr, nc, ndr, ndc))