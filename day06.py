banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def solve(banks):
    seen = []
    while True:
        index = banks.index(max(banks))
        value = banks[index]
        banks[index] = 0
        for x in range(1, value + 1):
            banks[(index+x)%len(banks)] += 1
        if banks in seen:
            break
        seen.append(list(banks))
    return len(seen)+1, banks

assert solve([0,2,7,0])[0] == 5
assert solve([2,4,1,2])[0]-1 == 4

cycles, curBanks = solve(banks)
print("Part 1: {}".format(cycles))
cycles2, _ = solve(curBanks)
print("part 2: {}".format(cycles2-1))
