with open("input.txt", "r") as file:
    data = file.read().splitlines()

# create 2d array 
matrix = list(list(line) for line in data)

directions = ['^','>','v','<']

def findIndex(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == directions[0]:
                return i,j
    
rowIdx, colIdx = findIndex(matrix)
direction = matrix[rowIdx][colIdx]

while rowIdx > 0 and colIdx > 0 and rowIdx < len(matrix) and colIdx < len(matrix[0]):
    if direction == directions[0]:
        matrix[rowIdx][colIdx] = 'X'
        if rowIdx - 1 < 0:
            break 
        if matrix[rowIdx-1][colIdx] == '#':
            direction = directions[(directions.index(direction) + 1) % 4] # circular rotation to change direction
        else:
            rowIdx -= 1 
    elif direction == directions[1]:
        matrix[rowIdx][colIdx] = 'X'   
        if colIdx + 1 >= len(matrix[0]):
            break
        if matrix[rowIdx][colIdx+1] == '#':
            direction = directions[(directions.index(direction) + 1) % 4] # circular rotation to change direction    
        else:
            colIdx += 1
    elif direction == directions[2]:
        matrix[rowIdx][colIdx] = 'X'
        if rowIdx + 1 >= len(matrix):
            break
        if matrix[rowIdx+1][colIdx] == '#':
            direction = directions[(directions.index(direction) + 1) % 4] # circular rotation to change direction    
        else:
            rowIdx += 1
    elif direction == directions[3] :
        matrix[rowIdx][colIdx] = 'X'
        if colIdx - 1 < 0:
            break 
        if matrix[rowIdx][colIdx-1] == '#':
            direction = directions[(directions.index(direction) + 1) % 4] # circular rotation to change direction    
        else:
            colIdx -= 1
    

positions = 0

for row in matrix:
    positions += row.count('X')

print(positions)