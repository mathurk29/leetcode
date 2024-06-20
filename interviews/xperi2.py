# """ Problem 1:
# Sunshine of a number

# Given a number, reduce the number to its smallest form if any of the digits sub-string is strictly increasing or decreasing by a difference of 1.
# Reduction by summing the sub-string in place.
# Consider each direction and distinct order as separate components.

# Consider left precedence for summing.

# Examples:
# 1985 ⇒ 1175
# 456 ⇒ 15
# 1212332 ⇒ 365 ⇒ 311

from typing import List


def isStrict(a, b):
    return True if (b == a + 1 or b == a - 1) else False


def isStrictIncreasing(a, b):
    return True if (b == a + 1) else False


def isStrictDecreasing(a, b):
    return True if (b == a - 1) else False


def getSunshine(num: List):

    aux = list()
    i = 0
    while i < len(num) - 1:

        j = i + 1
        while not isStrict(num[i], num[j]):
            j += 1

        # added the unstrict sublist to the result as it is
        aux.extend(num[i:j])

        # move i right to j
        i = j

        if i == len(num):  # if we have reached the end break
            return num

        # i and i + 1  are in some strict order
        j = i + 1

        # increase j untill the strictness is same as that of i and j.
        if isStrictIncreasing(num[i], num[j]):
            while isStrictIncreasing(num[j], num[j + 1]):
                j += 1

        elif isStrictDecreasing(num[i], num[j]):
            while isStrictDecreasing(num[j], num[j + 1]):
                j += 1

        # num = num[:i] + [sum(num[i:j+1])] + num[j+1:]

        aux.extend([sum(num[i : j + 1])])

        i = j + 1


getSunshine(num=[1, 2, 1, 2, 3, 3, 2])


# num = 1212332
# i = 0;
#    j = 1;  isStrictIncreasing(2,1) -> False;

# num = [] + [sum([0,2])] + num[2:]
# num = [] + [3] + [1,2,3,3,2]
# num = [3,1,2,3,3,2]


# i = 1
#
