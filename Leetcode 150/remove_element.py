# https://leetcode.com/problems/remove-element

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1
        return i

sol = Solution()
sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
    