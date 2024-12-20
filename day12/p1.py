from collections import deque # doubly ended queue

with open('input.txt', 'r') as file:
    data = file.read().strip()

grid = list(list(line) for line in data.splitlines())
rows = len(grid)
cols = len(grid[0])
regions = []
seen = set()
directions = [[0,1], [1,0], [-1,0], [0,-1]]
# floodfill(?)

def withinBoundaries(row, col):
    return 0 <= row < rows and 0 <= col < cols

for r in range(rows):
    for c in range(cols):
        if (r,c) in seen:
            continue
        seen.add((r,c))
        region = set()
        region.add((r,c))
        q = deque([(r,c)]) # explore the coordinates up, down, left, right of this (r,c)
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft() # current row and current col
            for dr, dc in directions:
                nr = cr + dr
                nc = cc + dc
                if not withinBoundaries(nr,nc):
                    continue
                if grid[nr][nc] != crop:
                    continue
                if (nr,nc) in region: # means it is already accounted for
                    continue
                region.add((nr,nc))
                q.append((nr,nc))
        seen |= region # set union - mark everything in region as seen 
        regions.append(region) # append a set of region for that particular crop

def perimeter(region):
    output = 0
    for (r,c) in region:
        output += 4 # since a square has 4 sides 
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if (nr,nc) in region:
                # 2 blocks side by side - 3 sides left, 3 blocks side by side - middle one 2 sides, 4 blocks side T shape - middle one 1 side, fully enclosed 5 blocks - middle one 0 sides
                output -= 1 
    return output 

sum = 0
for region in regions:
    sum += len(region) * perimeter(region)
    
print(sum)