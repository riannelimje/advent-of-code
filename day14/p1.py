with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

x = 101
y = 103
finalPos = []
for line in data:
    p,v = line.split()
    px =  int(p.split(',')[0][2:])
    py = int(p.split(',')[1])
    vx =  int(v.split(',')[0][2:])
    vy = int(v.split(',')[1])

    for i in range(100):
        px = (px + vx) % x
        py = (py + vy) % y
    finalPos.append((px,py))

q1,q2,q3,q4 = 0,0,0,0
# find the count for each quadrant
for px,py in finalPos:
    if 0<=px<x//2 and 0<=py<y//2:
        q1 += 1
    elif 0<=px<x//2 and y//2<py<y:
        q2 += 1
    elif x//2<px<x and 0<=py<y//2:
        q3 += 1
    elif x//2<px<x and y//2<py<y:
        q4 += 1

print(q1*q2*q3*q4)