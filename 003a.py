# checks to see if two squares overlap
def overlap(p, q):
    # check if on box is to the left of the other
    if p[1] > (q[1] + q[3]) or (q[1] + q[3]) > (p[1] + p[3]):
        return False

    # check for one above the other
    if p[2] > (q[2] + q[4]) or (q[2] + q[4]) > (p[2] + p[4]):
        return False

    return True
    
# gets square inches of overlapping areas
def overlapArea(p, q):
    area = 0 

    return area

# read in changes
file = open("input003.txt", "r")

claims = list()
overlaps = set()

# parse out data
for line in file:
    data = line.split()
    claim = data[0]
    x = int(data[2].split(",")[0])
    y = int(data[2].split(",")[1][:-1])
    w = int(data[3].split("x")[0])
    h = int(data[3].split("x")[1])
    claims.append([claim, x, y, w, h])

# cycle through all claims
while len(claims) > 0:
    check = claims.pop()
    
    for claim in claims:
        if overlap(check, claim):
            overlaps.add(claim[0])
            overlaps.add(check[0])


print(len(overlaps))
