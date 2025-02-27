def binary_search(arr, target):
    """
    Perform binary search to find the index of 'target' in the sorted array 'arr'.
    Returns the index of 'target' if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # there is only one element
        # or the target might be at exactly low or high position
        # or when the search space is reduced to one last element
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 5

index = binary_search(sorted_array, target_value)

if index != -1:
    print(f"Target {target_value} found at index {index}")
else:
    print(f"Target {target_value} not found in the array")
