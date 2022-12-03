result = 0
with open("data/day3.txt") as f:
    while True:
        line = f.readline()
        if not line: # End of file
            break
        size = int(len(line)/2)
        compartment1 = set(line[:size])
        compartment2 = set(line[size:])
        for c in compartment1:
            if c in compartment2:
                if c.islower():
                    result += ord(c) - 96 # 'a' has priority 1
                else:
                    result += ord(c) - 38 # 'A' har priority 27

print(result)