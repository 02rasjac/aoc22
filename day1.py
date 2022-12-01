elves = [0]
top_three = [0, 0, 0]

def handleTop(n):
    for i, x in enumerate(top_three):
        if n > x:
            top_three[i] = n
            top_three.sort(reverse=False)
            break
            
with open("data/day1.txt") as f:
    while True:
        line = f.readline()
        if not line:
            handleTop(elves[-1])
            break
        if line == "\n":
            handleTop(elves[-1])
            elves.append(0)
            continue
        elves[-1] += int(line)



print(sum(top_three))