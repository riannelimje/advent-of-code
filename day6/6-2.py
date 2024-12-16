from tqdm import tqdm # this tqdm shows a progress bar for visualisation quite cool 

with open("input.txt", "r") as file:
    data = file.read().splitlines()

# create 2d array 
matrix = list(list(line) for line in data)

dir = 0 # initial direction
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def findIndex(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                return i,j
    
guardRowIdx, guardColIdx = findIndex(matrix)

# keep a copy of initial guard position
i, j = guardRowIdx, guardColIdx

visited = set()

# simulate guards path + record visited positions
while True:
    visited.add((i, j))
    nextRow = directions[dir][0] + i
    nextCol = directions[dir][1] + j
    # if out of bounds
    if not (0 <= nextRow < len(matrix) and 0 <= nextCol < len(matrix[0])):
        break
    if matrix[nextRow][nextCol] == '#':
        dir = (dir + 1) % 4 # change direction
    else: 
        i, j = nextRow, nextCol


# check if placing an obstacle at (r,c) will cause a loop 
def checkLoop(r, c):
    if matrix[r][c] == '#':
        return False # since there is alr an obstacle
   
    i,j = guardRowIdx, guardColIdx
    dir = 0
    seen = set()
    # temp obstacle
    matrix[r][c] = '#'

    while True:
        if (i,j,dir) in seen:
            matrix[r][c] = '.' # change back to dot
            return True # there is a loop
       
        seen.add((i,j,dir))
        nextRow = directions[dir][0] + i
        nextCol = directions[dir][1] + j

        if not (0 <= nextRow < len(matrix) and 0 <= nextCol < len(matrix[0])):
            matrix[r][c] = '.' # change back to dot
            return False
        
        if matrix[nextRow][nextCol] == '#':
            dir = (dir + 1) % 4 # change direction
        else: 
            i, j = nextRow, nextCol
    
count = 0
for r,c in tqdm(visited):
    if r == guardRowIdx and c == guardColIdx:
        continue # skip guard's starting position
    if checkLoop(r,c):
        count += 1

print(count)