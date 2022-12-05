import re

n_stacks = 9
stack_string_len = n_stacks * 4
stacks = [[]] # Top to bottom
for n in range(1, n_stacks): # Initialize stack
    stacks.append([])

def readstack(line):
    stack_index = 0
    for i in range(1, stack_string_len, 4):
        # print(stack_index)
        if line[i].isalpha():
            stacks[stack_index].append(line[i])
        stack_index += 1

with open("data/day5.txt") as f:
    while True:
        line = f.readline().strip("\n")
        if not line: # End of file
            break
        if not line[1].isnumeric(): # Reached bottom of stack
            readstack(line)
        else:
            break

    # print(stacks)
    # Ingnore an empty line
    f.readline()
    instruction_line = [] # [0, 1, 2] Move 0 from stack 1 to stack 2

    while True:
        line = f.readline()
        if not line: # End of file
            break
        instruction_line = [int(c) for c in re.findall(r"\d+", line)]
        for x in range(0, instruction_line[0]):
            crate = stacks[instruction_line[1]-1].pop(0)
            stacks[instruction_line[2]-1].insert(0, crate)


print(stacks)

# Generate the code
code = ""
for stack in stacks:
    code += stack[0]
print(code)