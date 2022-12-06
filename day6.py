stream = None
with open("data/day6.txt") as f:
    stream = f.readline().strip("\n")

buffer = list(stream[:4]) # Hold the 4 latest characters (oldest to newest)

message_start_index = 3
for c in stream[4:]:
    message_start_index += 1
    buffer.pop(0) # Remove the oldest character
    buffer.append(c) # Add the new character to the end
    if len(set(buffer)) == 4: # 4 unique characters
        break

print(message_start_index+1)
