currentFrequency = 0
seenFrequencies = {0}
foundFrequency = False

# read in changes
file = open("input001.txt", "r")

# loop through changes
while not foundFrequency:
    for line in file:
        currentFrequency += int(line)
        if currentFrequency in seenFrequencies:
            foundFrequency = True
            break
        else:
            seenFrequencies.add(currentFrequency)
    file.seek(0)

file.close()

# report final frequency
print(currentFrequency)
