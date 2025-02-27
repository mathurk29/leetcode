# https://leetcode.com/problems/remove-duplicates-from-sorted-array


# Approach:
# As it is non-decreasing thus all duplicate elemets are stored next to each other - so Lets MARK the leftmost element as the unique
# Thus a unique element is one which is diff from it's left. (right may be duplicate or next unique element)
# Our approach is - traverse the array with i - and for every unique element (i.e. diff from it's predecessor) - overwrite kth value with it, and increment k.
# thus the first k values in array are overwritten with all our unique elements
# and we can return i.

class Solution:
    def removeDuplicates(self,nums):
        
        # since 0th element do not have any left we set convention that it is unique. Hence we have to start our overwriting from 1
        # it also works for edge case like [1,1,1,1,1,1,1] - where number of unique elements = 1 and  and we will return k unchanged as k = 1
        k = 1  

        # -1 because we will compare right element with left element to determine if right element is unique
        for i in range(len(nums) - 1):
            current = nums[i]
            right = nums[i + 1]

            if right != current:
                # right is unique
                nums[k] = right
                k += 1

        # question asked to in-place fix arr and return the number of unique elements.
        return k

sol = Solution()
sol.removeDuplicates([0,0,0,0,0,])