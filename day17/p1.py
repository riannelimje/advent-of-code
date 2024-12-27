import re

with open('input.txt', 'r') as file:
    data = file.read().strip()

register, program = data.split('\n\n')
a, b, c = map(int, re.findall(r"\d+", register))
program = list(map(int, re.findall(r"\d+", program)))

def combo(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a 
    if operand == 5:
        return b 
    if operand == 6:
        return c

pointer = 0
output = []
while pointer < len(program):
    ins = program[pointer]
    operand = program[pointer+1]
    if ins == 0:
        a = a >> combo(operand) # rightshift operator
    elif ins == 1:
        b = b ^ operand
    elif ins == 2:
        b = combo(operand) % 8
    elif ins == 3:
        if a != 0:
            pointer = operand
            continue
    elif ins == 4:
        b = b ^ c # XOR
    elif ins == 5:
        output.append(combo(operand) % 8)
    elif ins == 6:
        b = a >> combo(operand)
    elif ins == 7:
        c = a >> combo(operand)
    pointer += 2
    
print(",".join(map(str,output)))