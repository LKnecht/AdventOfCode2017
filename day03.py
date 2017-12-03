#
#  Part 1: Find the Manhattan Distance between n and 1 on the numberspiral
#
#  17  16  15  14  13
#  18   5   4   3  12
#  19   6   1   2  11
#  20   7   8   9  10
#  21  22  23---> ...

def layerSize(layer):
    return 8*(layer-1) if layer > 1 else 1

def layerIndex(n):
    sizeSum, layer = 0, 1
    while sizeSum < n:
        sizeSum += layerSize(layer)
        layer += 1
    return layer - 1

def lastNumberInLayer(layer):
    return (layer - 1) * layer * 4 + 1  # variation of gauss sum formula

def distToQuadrantMiddle(n, layer):
    quadSize = layerSize(layer) // 4
    lastNumInQuad = lastNumberInLayer(layer)
    while n < lastNumInQuad:
        lastNumInQuad -= quadSize
    return abs(quadSize // 2 + lastNumInQuad - n)

def ManhattanDistance(n):
    if n == 1: return 0
    layer = layerIndex(n)
    return layer + distToQuadrantMiddle(n, layer) - 1

assert(ManhattanDistance(1) == 0)
assert(ManhattanDistance(12) == 3)
assert(ManhattanDistance(23) == 2)
assert(ManhattanDistance(1024) == 31)

myInput = 277678
print("Part 1: {}".format(ManhattanDistance(myInput)))

#
# Part 2: The numberspiral is now build by building the sum of adajacent numbers
#         starting with only 1 in the middle.
#         What is the first value written larger than myInput?
#
#  147  142  133  122   59
#  304    5    4    2   57
#  330   10    1    1   54
#  351   11   23   25   26
#  362  747  806 --->   ...

def getNeighbourCoords(point):
    x, y = point
    d = [-1, 0, 1]
    res = []
    for dx in d:
        for dy in d:
            if dx == 0 and dy == 0: continue
            res.append((x+dx, y+dy))
    return res

def turnLeft(direction):
    return (-direction[1], direction[0])

def move(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

matrix = {(0,0): 1,
          (1,0): 1,
          (1,1): 2}

position = (1,1)
direction = (-1,0)
value = 0
while value < myInput:
    position = move(position, direction)
    value = 0
    for neighbourCoord in getNeighbourCoords(position):
        value += matrix.get(neighbourCoord, 0)
    matrix[position] = value
    newDir = turnLeft(direction)
    if matrix.get(move(position, newDir), None) is None:
        direction = newDir

print("Part 2: {}".format(value))
