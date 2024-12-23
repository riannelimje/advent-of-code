import re

with open('input.txt', 'r') as file:
    data = file.read().strip().split("\n\n")

tokens = 0
a = 3
b = 1

for line in data:
    pattern = r"\d+" # all digits 
    ax, ay, bx, by, px, py = map(int, re.findall(pattern, line))

    # given an equation of ax(i) + bx(j) = px and 
    # ay(i) + by(j) = py

    i = (py - ay * (px/ax)) / (by - ay * (bx/ax)) # this will be for button b
    j = (px - bx * i) / ax # this will be for button a 

    if round(i,2).is_integer() and round(j,2).is_integer():
        tokens += round(i) * b + round(j) * a

print(tokens)