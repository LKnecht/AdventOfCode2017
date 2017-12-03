#  Part 1: Find the Manhattan Distance between n and 1 on the numberspiral
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

def ManhattenDistance(n):
    if n == 1: return 0
    layer = layerIndex(n)
    return layer + distToQuadrantMiddle(n, layer) - 1

assert(ManhattenDistance(1) == 0)
assert(ManhattenDistance(12) == 3)
assert(ManhattenDistance(23) == 2)
assert(ManhattenDistance(1024) == 31)

print(ManhattenDistance(277678))
