# https://leetcode.com/problems/product-of-array-except-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,3,4] \n

        loop through input from left to right \n
        answer[i] = answer[i-1] * num[i-1] \n
        [1,1,2,6] \n

        answer[i] *= num[]

        [24,12,8,6]
        """
        temp = 1
        answer = len(nums) * [1]
        temp2 = 1

        for left in range(1, len(nums)):
            answer[left] = answer[left - 1] * nums[left - 1]
        for right in range(len(nums) - 1, -1, -1):
            answer[right] *= temp2
            temp2 *= nums[right]

        return answer


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         """
#         make prefix array \n
#         make postfix array \n
#         make result array \n

#         [1,2,3,4] \n

#         loop through input from left to right \n
#         ith prefix = i-1 st prefix * i-1st input \n
#         [1,1,2,6] \n

#         loop through input from right to left \n
#         ith postfix = i+1 st postfix * i+1 st input \n
#         [24,12,4,1] \n

#         result[i] = prefix[i] * postfix[i] \n
#         [24,12,8,6] \n
#         """
#         prefix_array = len(nums) * [1]
#         postfix_array = len(nums) * [1]
#         answer = len(nums) * [1]

#         for left in range(1, len(nums)):
#             prefix_array[left] = prefix_array[left - 1] * nums[left - 1]

#         for right in range(len(nums) - 1 - 1, -1, -1):
#             postfix_array[right] = postfix_array[right + 1] * nums[right + 1]

#         for i in range(len(nums)):
#             answer[i] = prefix_array[i] * postfix_array[i]

#         return answer

sol = Solution()

assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
