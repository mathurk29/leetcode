from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # if n == 1:
        #     return 0

        # below is better

        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]: # n-1 is last element stupid - not n.
            return n

        # search remaining array now
        left_pointer = 1
        right_pointer = n - 2

        while left_pointer <= right_pointer: # use <= in binary search
            mid_pointer = (left_pointer + right_pointer) // 2 # calculate mid_pointer inside while
            if self.isPeak(nums, mid_pointer, n):
                return mid_pointer
            if nums[mid_pointer] < nums[mid_pointer + 1]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1

    def isPeak(self, nums, location, n):
        ## NOT required following as special quick cases are identified and handled at the start of prog.

        # if location == 0:
        #     return nums[location] > nums[location + 1]
        # if location == n-1:
        #     return nums[location - 1] < nums[location]
        return (
            nums[location - 1] < nums[location] and nums[location + 1] < nums[location] # middle element has to be greater than neigbor - NOT _ < _ < _
        )

sol = Solution()
# assert sol.findPeakElement([1, 2, 3, 1]) == 2
assert sol.findPeakElement([1, 2]) == 1
