hand_value = {"A": 1, "B": 2, "C": 3}
player_score = 0

with open("data/day2.txt") as f:
    while True:
        line = f.readline()
        if not line: # End of file
            break
        elfe = line[0]
        user = chr(ord(line[2]) - 23) # Convert user's hand to A, B, C for easier compairson
        if user == elfe:
            # points = 3 (draw) + points from hand (X becomes A when testing, ASCII-value of 65)
            player_score += 3 + hand_value[user]
        elif (user == "A" and elfe == "C") or (user == "B" and elfe == "A") or (user == "C" and elfe == "B"):
            # Player wins
            player_score += 6 + hand_value[user]
        else:
            # Player loses
            player_score += hand_value[user]

# Subtract 23 from user (X, Y, Z) to (a, b, c)
# If same => draw
# Else if (a and C) or (b and A) or (c and B) => user wins
# Else elfe wins

print(player_score)
