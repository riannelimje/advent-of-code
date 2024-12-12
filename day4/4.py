with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines() #strip of whitespace 

grid = [list(line) for line in data]
rows = len(grid)
cols = len(grid[0])
target = "XMAS"
targetLen = len(target)
count = 0

# ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M']
# ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A']
# set direction to search the grid (row,col)
directions = [
    (0,1), #right
    (1,0), #down
    (-1,0), #up
    (0,-1), #left
    (1,1), #down right
    (-1,1), #up right
    (-1,-1), #up left
    (1,-1), #down left
]

# check boundaries 
def isValid(row,col):
    return 0<=row<rows and 0<=col<cols

for row in range(rows):
    for col in range(cols):
        for dr, dc in directions: # will move in the specified direction
            matches = True
            for i in range(targetLen):
                newRow = row + i*dr 
                newCol = col + i*dc
                if not (isValid(newRow,newCol) and grid[newRow][newCol] == target[i]):
                    matches = False
                    break
            if matches:
                count += 1
print(count)