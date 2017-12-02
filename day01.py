# Find the sum of all digits that match the next digit

def test():
    tests = {"1122": 3,
             "1111": 4,
             "1234": 0,
             "912121219": 9}
    for inp, sol in tests.items():
        if matchSum(inp) != sol:
            print("{} gave {} instead of {}".format(inp, matchSum(inp), sol))
            return False
    print("{} tests passed".format(len(tests)))
    return True

def matchSum(digits):
    digits += digits[0]
    return sum([int(digits[i]) if digits[i] == digits[i+1] else 0
                for i in range(len(digits)-1)])

test()
