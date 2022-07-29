# arr  = [1,2,3,4,5,6,7,8,0,-1,-2,-3,-4,-5,-6,-7]  k = 3
arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, -1, -2, -3, -4, -5, -6, -7]


def peakElement(arr):
    '''
        returns the peak element of the array - first increasing -> later decreasing

    '''

    if len(arr) < 3:
        return max(arr)

    mid = len(arr) // 2

    # check if peak
    if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
        return arr[mid]

    # ascending slope
    elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
        peakElement(arr[mid:])

    # descending slope
    elif arr[mid - 1] > arr[mid] > arr[mid + 1]:

        peakElement(arr[:mid+1])


print(peakElement(arr))

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, -1, -2, -3, -4, -5, -6, -7]

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, -1]

# 5 < 6 and 6 > 7
# 5 < 6  <  7


# arr = [6, 7, 8, 0, -1]
