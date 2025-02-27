# find nth root of a give number floored to nearest integer

def nth_root(num: int, n:int):
    
    low = 1
    high = num
    res = num

    while low < high:
        mid = (low + high ) // 2
        if mid ** n <= num:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res