currentFrequency = 0

# read in changes
file = open("input001.txt", "r")

# loop through changes
for line in file:
    currentFrequency += int(line)

# report final frequency
print (currentFrequency)