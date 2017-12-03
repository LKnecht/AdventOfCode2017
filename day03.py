#  Part 1: Find the Manhattan Distance between n and 1 on the numberspiral
#  17  16  15  14  13
#  18   5   4   3  12
#  19   6   1   2  11
#  20   7   8   9  10
#  21  22  23---> ...

def layerSize(l):
    return 8*(l-1) if l > 1 else 1

def layerIndex(n):
    s, l = 0, 1
    while s < n:
        s += layerSize(l)
        l += 1
    return l - 1

def lastNumberInLayer(l):
    return (l - 1) * l * 4 + 1  # variation of gauss sum formula

def distToQuadrantMiddle(n, l):
    quadSize = layerSize(l) // 4
    lln = lastNumberInLayer(l)
    while n < lln:
        lln -= quadSize
    return abs(quadSize // 2 + lln - n)

def ManhattenDistance(n):
    if n == 1: return 0
    l = layerIndex(n)
    return l + distToQuadrantMiddle(n, l) - 1

assert(ManhattenDistance(1) == 0)
assert(ManhattenDistance(12) == 3)
assert(ManhattenDistance(23) == 2)
assert(ManhattenDistance(1024) == 31)

print(ManhattenDistance(277678))
