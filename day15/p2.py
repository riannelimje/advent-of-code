with open('input.txt', 'r') as file:
    data = file.read().strip()

warehouse, movements = data.split("\n\n")

expansion = {'#': '##', 'O': "[]", '.': '..', '@': '@.'}

grid = list(list("".join(expansion[char] for char in line)) for line in warehouse.splitlines())
movements = "".join(movements.splitlines())

n = len(grid)
m = len(grid[0])
directions = {'^':(-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def findRobot():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                return i,j

i, j = findRobot()

for move in movements:
    r, c = directions.get(move)
    targets = [(i,j)]
    go = True
    for cr, cc in targets:
        nr = cr + r
        nc = cc + c
        if (nr,nc) in targets:
            continue
        char = grid[nr][nc]
        if char == '#':
            go = False
            break
        if char == '[':
            targets.append((nr,nc))
            targets.append((nr,nc+1)) # for the ]
        if char == ']':
            targets.append((nr,nc))
            targets.append((nr,nc-1)) # for the [
    if not go:
        continue
    copy = [list(row) for row in grid]
    grid[i][j] = '.'
    grid[i+r][j+c] = '@'
    for br, bc in set(targets[1:]):
        grid[br][bc] = '.' # clear old position
    for br, bc in set(targets[1:]):
        grid[br+r][bc+c] = copy[br][bc] # move to new position
    i += r
    j += c
  
sum = 0
for row in range(1,n):
    for col in range(1,m):
        if grid[row][col] == '[':
            sum += row * 100 + col 

for row in grid:
    print("".join(row))

print(sum)