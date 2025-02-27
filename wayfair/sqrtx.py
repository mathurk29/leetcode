# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 1, x // 2 -1
        while low < high:
            mid = (low + high) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return (low + high) //2



## Dry run

# x = 8
# low   high    low < high     mid    mid*mid < x     [T/F]
