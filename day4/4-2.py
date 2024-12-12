with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines() 

grid = [list(line) for line in data]
rows = len(grid)
cols = len(grid[0])
count = 0

for row in range(1, rows-1):
    for col in range(1, cols-1):
       if grid[row][col] == 'A':
           corner1 = grid[row-1][col-1] #left up
           corner2 = grid[row+1][col-1] #left down
           corner3 = grid[row-1][col+1] #right up
           corner4 = grid[row+1][col+1] #right down

           word1 = corner1 + 'A' + corner4
           word2 = corner2 + 'A' + corner3

           if word1 in ['MAS','SAM'] and word2 in ['MAS','SAM']:
               count +=1 
          
print(count)