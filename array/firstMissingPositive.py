from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


sol = Solution()

testcases = [
    # [0],
    # [-1],
    # [-1,-2],
    # [0, -1,-2],
    # [1],
    # [2],
    # [3],
    # [0,1],
    # [0,2],
    # [23,345345,6575678,0]
    [3, 4, -1, 1]
]

for testcase in testcases:
    sol.firstMissingPositive(testcase)
