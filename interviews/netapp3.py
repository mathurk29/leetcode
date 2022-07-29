
arr = [3, 4, -7, 2, 6, -1]


def kadaneAlgo(arr):

    max_so_far = -100000

    max_ending_here = 0

    for i in range(len(arr)):

        max_ending_here += arr[i]
        max_so_far = max(max_so_far, max_ending_here)

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


kadaneAlgo(arr)

# aside
