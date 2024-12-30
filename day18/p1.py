from collections import deque

with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

n = 71 
m = 71 
bytes = 1024
directions = [[0,1], [1,0], [-1,0], [0,-1]]
ls = []

for line in data:
    x, y = line.split(',')
    ls.append(map(int, (y,x)))

def withinBoundaries(i,j):
    return 0 <= i < n and 0 <= j < m

grid = [["." for _ in range(n)] for _ in range(m)]
for i,j in ls[:bytes]:
    grid[i][j] = '#'

q = deque([(0,0,0)]) # row, col, steps
seen = {(0,0)}
while q: 
    r, c, steps = q.popleft()
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc 
        if not withinBoundaries(nr,nc):
            continue
        if grid[nr][nc] == '#':
            continue
        if (nr,nc) in seen:
            continue
        if nr == nc == n-1:
            print(steps+1)
            exit()
        seen.add((nr,nc))
        q.append((nr,nc,steps+1))

# for row in grid:
#     print(''.join(row))