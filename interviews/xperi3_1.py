# Coding question: Given an array of either type A or Type B, find peak value or
# valley value respectively from it.
# Example A= [1,12,8,6,5,3,1] , B = [13,4,2,5,7,9,11]


# Constraint A,B >= 3
# all are > 0 -> typeB

# for type A -> compare with left and right -> if both are small then it is peak point
#  left > mid > right  left subarray
#


# for type B -> compare with left and right -> if both are big then it is valley point


def checkType(array):

    return "A" if array[0] < array[1] else "B"


def findPeak(array):

    middle_idx = len(array) // 2

    # peak
    if (
        array[middle_idx - 1] < array[middle_idx]
        and array[middle_idx] > array[middle_idx + 1]
    ):
        return array[middle_idx]

    # peak on right side
    if array[middle_idx - 1] < array[middle_idx] < array[middle_idx + 1]:
        return findPeak(array[middle_idx:])

    else:
        return findPeak(array[:middle_idx])


def findValley():
    pass


def main(array):

    return findPeak(array) if checkType(array) == "A" else findValley(array)


main(array=[1, 12, 8, 6, 5, 3, 1])

# mid = 3, 8 | 6 | 5
