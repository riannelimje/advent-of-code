with open('input.txt', 'r') as file:
    data = file.read().splitlines()

grid = list(list(map(int,line)) for line in data)
n = len(grid)
m = len(grid[0])

directions = [
    (-1,0), # up 
    (1,0), # down
    (0,-1), # left
    (0,1) # right
]

def checkBoundaries(row, col):
    return 0<=row<n and 0<=col<m

# need to do dfs
def score(i, j):
    # check if it's a valid trailhead
    if grid[i][j] != 0:
        return 0
    
    ans = 0 
    stack = [(i,j)] # position to explore next 
    visited = set()

    while stack:
        curi, curj = stack.pop()

        # i just need to comment this out to get the answer
        # if (curi, curj) in visited:
        #     continue
        # visited.add((curi,curj))

        currNum = grid[curi][curj]
        if currNum == 9:
            ans += 1
            continue

        # go thru all of the neighbours
        for dr, dc in directions:
            newi = curi + dr
            newj = curj + dc

            if not checkBoundaries(newi,newj):
                continue

            neighbour = grid[newi][newj]
            if neighbour != currNum +1:
                continue
            stack.append((newi,newj))
    
    return ans

res = 0
for i in range(n):
    for j in range(m):
        res += score(i,j)
print(res)