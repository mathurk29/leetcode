from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(float("+inf"))

        def fill_with_none(num):
            if num is None:
                return

            if not (0 < num < len(nums)):
                return

            next_num = nums[num]
            nums[num] = None
            fill_with_none(next_num)

        for num in nums:
            if num is not None:
                fill_with_none(num)

        for i, num in enumerate(nums[1:], start=1):
            if num is not None:
                return i

        return len(nums)


testcases = [
    # [0], 
    # [-1],
    # [-1, -2],
    # [0, -1, -2],
    # [1],
    # [2],
    # [3],
    # [0, 1],
    # [0, 2],
    # [23, 345345, 6575678, 0],
    [3,4,-1,1]
]

sol = Solution()

for testcase in testcases:
    sol.firstMissingPositive(testcase)
