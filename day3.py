result = 0
with open("data/day3.txt") as f:
    while True:
        line1 = set(f.readline())
        line2 = set(f.readline())
        line3 = set(f.readline())
        if not line1: # End of file
            break
        
        for c in line1:
            if c != "\n" and c in line2 and c in line3: # The item is in all 3 bags
                if c.islower():
                    result += ord(c) - 96 # 'a' has priority 1
                else:
                    result += ord(c) - 38 # 'A' har priority 27

print(result)