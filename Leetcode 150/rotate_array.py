# https://leetcode.com/problems/rotate-array/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        extra_k = k % len(nums)
        nums[:] = nums[-extra_k:] + nums[:-extra_k] # Done :)