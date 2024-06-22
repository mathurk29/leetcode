# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray1(self, nums: List[int]) -> int:
        """Solution by Kshitij"""
        length = len(nums)
        result = 0
        i = 0
        while i < length:
            if nums[i] != 1:
                i += 1
                continue
            j = i + 1
            while j < length and nums[j] == 1:
                j += 1
            # j is at first non-one number.
            left_window = j + 1
            if j + 1 < length and nums[j + 1] == 1:  # 1's are avl after next number
                j += 1
                while j + 1 < length and nums[j + 1] == 1:
                    j += 1
                # j is at last one number
            result = max(result, j - i)
            i = left_window
        if result == len(nums):
            result -= 1
        return result

    def longestSubarray(self, nums: List[int]) -> int:
        """
        dp[i][0] be the length of longest subarray of ones, such that it ends at point i \n
        dp[i][1] be the length longest subarray, which has one zero and ends at point i
        """

        n = len(nums)
        if sum(nums) == n: return n - 1 # all are `1`

        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = nums[0]

        for i in range(1,n):
            pass
            if nums[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
            if nums[i] == 0:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]

        return max([i for j in dp for i in j])


sol = Solution()
assert sol.longestSubarray([1, 1, 0, 1]) == 3
assert sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
assert sol.longestSubarray([1, 1, 1]) == 2
assert sol.longestSubarray([1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]) == 11
