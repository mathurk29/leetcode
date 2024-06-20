# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = set()
        for i in range(len(nums)):
            if i > k:
                hash.remove(nums[i - k - 1])
            if nums[i] in hash:
                return True
            else:
                hash.add(nums[i])


# i - j <= k
# i <= j + k
# abs(-j) <= k
# j <= k
# thus j goes upto k thus range_stop = k + 1


sol = Solution()
# sol.containsNearbyDuplicate(nums=[2, 2], k=3)
# sol.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
sol.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
