# https://leetcode.com/problems/jump-game

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # i is at last index
        i = len(nums) - 1
        j = i -1
        while i >= 0 and j >= 0:  # i =4 , j =3
            # j is at one left to i
            if nums[j] >= (i - j):  # 1 >=1
                i = j # i = 3, j =3
                j = i -1
            else:
                j -= 1
        return i == 0