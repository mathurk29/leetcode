# https://leetcode.com/problems/median-of-two-sorted-arrays/


def medianSortedLists(A, B):

    l = len(A) + len(B)

    return (
        binarySearch(A, B, l // 2)
        if l % 2 == 1
        else (binarySearch(A, B, (l // 2) - 1) + binarySearch(A, B, l // 2)) / 2
    )


def binarySearch(A, B, k):

    if not A:
        return B[k]
    if not B:
        return A[k]

    middle_a = len(A) // 2
    middle_b = len(B) // 2

    if middle_a + middle_b < k:

        if A[middle_a] > B[middle_b]:
            return binarySearch(A, B[middle_b + 1 :], k - middle_b - 1)

        else:

            return binarySearch(A[middle_a + 1 :], B, k - middle_a - 1)

    else:

        if A[middle_a] > B[middle_b]:
            return binarySearch(A[:middle_a], B, k)

        else:
            return binarySearch(A, B[:middle_b], k)


# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


# nums1 = [1 ,3, ,5, ,7, 9 ,11 ]
# nums2 = [2, 4, 6, 8, 10, 12 ]
# 1,2,3,4,5,6,7,8,9,10,11,12
# 6 + 7 / 2


# a = [1, 2, 3, 4]
# b = [5, 6, 7]


a = [1, 3]
b = [2, 4, 8, 9, 12, 14, 16]


print(medianSortedLists(a, b))


# aditya.gupta@olx.com
