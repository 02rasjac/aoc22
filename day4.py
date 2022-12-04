sections = []
n_fully_contained = 0
with open("data/day4.txt") as f:
    while True:
        line = f.readline()
        if not line: # End of file
            break
        line = line.replace('\n', '')
        # Seperate each boundary
        line = line.split(',')
        pair = [line[0].split('-'), line[1].split('-')]

        if (int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1])) or (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1])):
            n_fully_contained += 1

print(n_fully_contained)