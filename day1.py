elves = [0]
with open("data/day1.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == "\n":
            elves.append(0)
            continue
        elves[-1] += int(line)

print(max(elves))