
# psudo code:
# ```
# def merge_sort(l,h):
#     if l < h:
#         mid = (l + h ) // 2
#         merge_sort(l, mid)k
#         merge_sort(mid+1,h)
#         merge(l,mid,h)
# ```

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge two sorted halves
    sorted_arr = []
    i = j = 0

    # Compare elements from left and right half and append smaller one
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    # Append remaining elements from left half, if any
    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1

    # Append remaining elements from right half, if any
    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1

    return sorted_arr