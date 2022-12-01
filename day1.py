elves = [0]
top_three = [0, 0, 0]

def handleTop(n):
    """Keep order of the top three elves"""
    for i, x in enumerate(top_three):
        if n > x:
            top_three[i] = n
            # Sort the list in ascending order so the function replaces the first element that smaller, if any
            top_three.sort()
            break
            
with open("data/day1.txt") as f:
    while True:
        line = f.readline()
        if not line: # End of file
            handleTop(elves[-1])
            break
        if line == "\n": # End of elfe
            handleTop(elves[-1])
            elves.append(0)
            continue
        elves[-1] += int(line) # Sum the calories for the current elfe

# Print result
print(sum(top_three))