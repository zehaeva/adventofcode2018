from collections import Counter

twiceCount = 0
thriceCount = 0

# read in changes
file = open("input002.txt", "r")

# loop through changes
for line in file:
    twice = False
    thrice = False
    letters = list(line)
    c = Counter(letters)

    for x in c:
        if c[x] == 2:
            twice = True
        if c[x] == 3:
            thrice = True

    if twice:
        twiceCount += 1
    if thrice:
        thriceCount += 1

file.close()

print("Checksum: {}".format(twiceCount * thriceCount))