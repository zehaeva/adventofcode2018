class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Claim:
    number = ""
    ul = Point(0, 0)
    ur = Point(0, 0)
    ll = Point(0, 0)
    lr = Point(0, 0)
    w = 0
    h = 0

    def __init__(self, number, x, y, w, h):
        self.number = number
        self.ul = Point(x, y)
        self.ur = Point(x + w, y)
        self.ll = Point(x, y + h)
        self.lr = Point(x + w, y + h)
        self.w = w
        self.h = h

    # checks to see if two squares overlap
    def overlap(self, q):
        # check if on box is to the left of the other
        if self.ul.x > q.ur.x or q.ul.x > self.ur.x:
            return False
    
        # check for one above the other
        if self.ul.y > q.ll.y or q.ul.y > self.ll.y:
            return False
    
        return True

    # gets square inches of overlapping areas
    def overlap_area(self, q):
        width = 0
        height = 0
        return width * height


# read in changes
file = open("input003.txt", "r")

claims = list()
area = 0

# parse out data
for line in file:
    data = line.split()
    claim = Claim()
    claim.number = data[0]
    claim.x = int(data[2].split(",")[0])
    claim.y = int(data[2].split(",")[1][:-1])
    claim.w = int(data[3].split("x")[0])
    claim.h = int(data[3].split("x")[1])
    claims.append(claim)

# cycle through all claims
while len(claims) > 0:
    check = claims.pop()
    
    for claim in claims:
        if check.overlap(claim):
            area += check.overlap_area(claim)


print(area)
