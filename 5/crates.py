with open('5/input.txt') as f:
    lines = f.readlines()

with open('5/instructions.txt') as f:
    instructions = f.readlines()

stacks = []

def init_stacks():
    stacks = [[None for i in range(0)]for j in range(10)]
    for line in lines:
        for i in range(1,len(line), 4):
            if line[i].isdigit():
                return stacks
            if line[i]!=" ":
                BottomInsert(stacks[(i-1)//4], line[i])
                #stacks[(i-1)//4].append(line[i])
    return stacks

def extract_values_from_line(line: str):
    values = line.split(" ")
    changed_values = []
    changed_values.append(int(values[1]))
    changed_values.append(int(values[3]))
    changed_values.append(int(values[5][0]))
    return changed_values

def execute_instruction(values: list, stacks):
    for i in range(values[0]):
        value = stacks[values[1]-1].pop()
        stacks[values[2]-1].append(value)
    return stacks

def execute_instruction_part2(values: list, stacks):
    temp = []
    for i in range(values[0]):
        temp.append(stacks[values[1]-1].pop())
        if i == values[0]-1:
            for j in range(len(temp)):
                stacks[values[2]-1].append(temp.pop())
    return stacks

def BottomInsert(s, value):
    if not s:
        s.append(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.append(popped)

def main():
    stacks = init_stacks()
    print(stacks)
    for instruction in instructions:
        values = extract_values_from_line(instruction)
        stacks = execute_instruction(values, stacks)
    print("\n")
    print(stacks)
    total_string = ""
    for stack in stacks:
        if stack:
            total_string+=stack.pop()
    print(total_string)

def main_part2():
    stacks = init_stacks()
    print(stacks)
    for instruction in instructions:
        values = extract_values_from_line(instruction)
        stacks = execute_instruction_part2(values, stacks)
    print("\n")
    print(stacks)
    total_string = ""
    for stack in stacks:
        if stack:
            total_string+=stack.pop()
    print(total_string)

main_part2()