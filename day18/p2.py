from collections import deque

with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

n = 70
m = 70
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
ls = []

for line in data:
    x, y = line.split(',')
    ls.append(list(map(int, (y, x))))  # need to convert map to a list 

def withinBoundaries(i, j):
    return 0 <= i < n+1 and 0 <= j < m+1  

def isConnected(b):  
    grid = [["." for _ in range(n+1)] for _ in range(m+1)]
    for i, j in ls[:b]:
        grid[i][j] = '#'

    q = deque([(0, 0, 0)])  # row, col, steps
    seen = {(0, 0)}
    while q: 
        r, c, steps = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not withinBoundaries(nr, nc):
                continue
            if grid[nr][nc] == '#':
                continue
            if (nr, nc) in seen:
                continue
            if nr == n and nc == m: 
                return True
            seen.add((nr, nc))
            q.append((nr, nc, steps + 1))
    return False

# binary search
lo = 0
hi = len(ls) - 1

while lo < hi:
    mi = (lo + hi) // 2
    if isConnected(mi + 1):
        lo = mi + 1
    else:
        hi = mi  
        
print(ls[lo]) # rmb to swap the placement of the coordinates when keying in the answer