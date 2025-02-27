# https://leetcode.com/problems/remove-duplicates-from-sorted-array


# Approach:
# As it is non-decreasing thus all duplicate elemets are stored next to each other - so Lets MARK the leftmost element as the unique
# Thus a unique element is one which is diff from it's left. (right may be duplicate or next unique element)
# Our approach is - traverse the array with j - and for kth every unique element - overwrite kth value with it.
# thus the first k values in array are overwritten with all our unique elements
# and we can return i.

class Solution:
    def removeDuplicates(self,nums):
        k = 1  # since 0th element do not have any left we set convention that it is unique. Hence we have to start our overwriting from 1

        # -1 because we will compare right element with left element to determine if right element is unique
        for i in range(len(nums) - 1):
            current = nums[i]
            right = nums[i + 1]

            if right != current:
                # right is unique
                nums[k] = right
                k += 1

        # question asked to in-place fix arr and retrun the len of unique elements.
        return k
