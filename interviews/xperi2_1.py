def isStrict(a, b):
    return True if (b == a + 1 or b == a - 1) else False


def isStrictIncreasing(a, b):
    return True if (b == a + 1) else False


def isStrictDecreasing(a, b):
    return True if (b == a - 1) else False


def hasOrder(num):
    for i in len(num):
        if isStrict(num[i], num[i + 1]):
            return True
    return False


def getSunshine(num):
    if not hasOrder(num):
        return num

    i = 0
    while i < len(num):

        # ith loc do not have a window

        while i + 1 < len(num) and not isStrict(num[i], num[i + 1]):
            i += 1

        # ith loc have a window
