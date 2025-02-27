# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[k] and nums[i] == nums[k - 1]:
                continue
            k += 1
            nums[k] = nums[i]
        # return number of elements which is 1 + list index upto which the resultant array is valid
        return k + 1


# Driver code
nums = [1, 1, 1, 2, 2, 3]
sol = Solution()
print(sol.removeDuplicates(nums))  # Expected output: 5
