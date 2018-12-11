# read in changes
file = open("input002.txt", "r")

listOne = list()
listTwo = list()

# loop through changes
for line in file:
    letters = list(line)

    listOne.append(letters)
    listTwo.append(letters)

file.close()

lineLength = len(listOne[0])
found = False
foundX = ""
foundY = ""

for x in listOne:
    for y in listTwo:
        differences = 0
        for i in range(0, lineLength):
            if x[i] != y[i]:
                differences += 1
            if differences > 1:
                break

        if differences == 1:
            found = True
            foundX = x
            foundY = y
            break
    if found:
        break

print("X: {}".format("".join(foundX)))
print("Y: {}".format("".join(foundY)))
