hand_value = [1, 2, 3] # Rock, Paper, Scissor
player_score = 0

with open("data/day2.txt") as f:
    while True:
        line = f.readline()
        if not line: # End of file
            break
        elfe = line[0]
        ending = line[2]
        if ending == "X":
            player_score += hand_value[ord(elfe) - 66] # Loss, index for score A is -1
        elif ending == "Y":
            player_score += 3 + hand_value[ord(elfe) - 65] # Draw, index for A is 0
        else:
            player_score += 6 + hand_value[ord(elfe) - 67] # Win, index for score A is -2

# Subtract 23 from user (X, Y, Z) to (a, b, c)
# If same => draw
# Else if (a and C) or (b and A) or (c and B) => user wins
# Else elfe wins

print(player_score)
