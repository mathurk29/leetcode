# make prefix array
# make postfix array
# make result array

# [1,2,3,4]

# loop through input from left to right
# ith prefix = i-1 st prefix * i-1st input
# [1,1,2,6]

# loop through input from right to left
# ith postfix = i+1 st postfix * i+1 st input
# [24,12,4,1]

# result[i] = prefix[i] * postfix[i]
# [24,12,8,6]


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = len(nums) * [1]
        postfix_array = len(nums) * [1]
        answer = len(nums) * [1]

        for left in range(1, len(nums)):
            prefix_array[left] = prefix_array[left - 1] * nums[left - 1]

        for right in range(len(nums) - 1 - 1, -1, -1):
            postfix_array[right] = postfix_array[right + 1] * nums[right + 1]

        for i in range(len(nums)):
            answer[i] = prefix_array[i] * postfix_array[i]

        return answer


sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])
