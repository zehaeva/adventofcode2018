class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


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

    def __str__(self):
        return "{} @ {} {}x{}".format(self.number, self.ul, self.w, self.h)

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
        width = min(self.lr.x, q.lr.x) - max(self.ul.x, q.ul.x) 
        height = min(self.lr.y, q.lr.y) - max(self.ul.y, q.ul.y) 

        return width * height


class Cloth:
    reserved = [["." for n in range(0, 1000)] for n in range(0, 1000)]

    def __init(self):
        pass

    def reserve(self, claim):
        for x in range(claim.ul.x, claim.ur.x):
            for y in range(claim.ul.y, claim.ll.y):
                if self.reserved[x][y] == ".":
                    self.reserved[x][y] = claim.number
                else:
                    self.reserved[x][y] = "X"
    
    def conflicts(self):
        area = 0
        for x in range(0, 1000):
            for y in range(0, 1000):
                if self.reserved[x][y] == "X":
                    area += 1
        return area

    def find_conflict(self, claim):
        found = False
        for x in range(claim.ul.x, claim.lr.x):
            for y in range(claim.ul.y, claim.lr.y):
                if self.reserved[x][y] == "X":
                    found = True
                    break

            if found:
                break

        return found


# read in changes
file = open("input003.txt", "r")

claims = list()
area = 0
cloth = Cloth()

# parse out data
for line in file:
    data = line.split()
    claim = Claim(data[0],
                  int(data[2].split(",")[0]),
                  int(data[2].split(",")[1][:-1]),
                  int(data[3].split("x")[0]),
                  int(data[3].split("x")[1]))
    cloth.reserve(claim)
    claims.append(claim)

area = cloth.conflicts()

print("area {}".format(area))

# check for the one that does not have any conflicts
while len(claims) > 0:
    claim = claims.pop()
    if not cloth.find_conflict(claim):
        print("{}".format(claim))