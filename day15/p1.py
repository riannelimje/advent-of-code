with open('input.txt', 'r') as file:
    data = file.read().strip()

warehouse, movements = data.split("\n\n")

warehouse = list(list(line) for line in warehouse.splitlines())
movements = "".join(movements.splitlines())

n = len(warehouse)
m = len(warehouse[0])
directions = {'^':(-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def findRobot():
    for i in range(n):
        for j in range(m):
            if warehouse[i][j] == '@':
                return i,j
            
def canMove(i,j):
    if warehouse[i][j] == '#':
        return False
    return True

i, j = findRobot()
# i have to check if there is a box, whether i can move the box, move it if can - will also have a chain reaction
for move in movements:
    r, c = directions.get(move)
    nr = i + r
    nc = j + c
    while canMove(nr,nc):
        # try to find the first . after the last O
        if warehouse[nr][nc] == '.':
            warehouse[nr][nc] = 'O' # swap the first box into the empty space instead 
            warehouse[i][j] = '.' 
            i += r
            j += c
            warehouse[i][j] = '@'
            break 
        nr += r
        nc += c

sum = 0
for row in range(1,n):
    for col in range(1,m):
        if warehouse[row][col] == 'O':
            sum += row * 100 + col 

for row in warehouse:
    print("".join(row))

print(sum)