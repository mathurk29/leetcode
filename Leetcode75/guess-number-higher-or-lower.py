# https://leetcode.com/problems/guess-number-higher-or-lower


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    global pick
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = (
            1,
            n,
        )  # realise you are not gettting array of n elements - you are getting a single int n >= 1.
        mid = (left + right) // 2
        g = guess(mid)
        while g:
            if g == -1:  # go left
                right = mid
                mid = (left + right) // 2
            if g == 1:  # go right
                left = mid + 1
                mid = (left + right) // 2
            g = guess(mid)
        return mid

    def guessNumber2(self, n: int) -> int:
        left, right = (
            1,
            n,
        )  # realise you are not gettting array of n elements - you are getting a single int n >= 1.
        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == -1:  # go left
                right = mid
            if g == 1:  # go right
                left = mid + 1
        return mid

    # https://leetcode.com/problems/guess-number-higher-or-lower/solutions/84677/2-lines-as-usual-1-line-in-2022
    def guessNumber3(self, n):
        lo, hi = 1, n
        while lo < hi:  # since we are making (mid,mid) below
            mid = (lo + hi) // 2
            # 0 1 2(-1 )
            lo, hi = ((mid, mid), (mid + 1, hi), (lo, mid - 1))[
                guess(mid)
            ]  # tricky (mid,mid) - see in BS when mid is matched to the number to be found - we stop. We can say that next imaginary step would be low=mid, right=mid
        return lo


pick = 10
sol = Solution()
print(sol.guessNumber(10))
