# https://leetcode.com/problems/merge-sorted-array

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # deal with edge case of empty lists
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        
        # we cannot start from left end - as if nums2[j] < nums1[i], we will have to shift all elements in nums1 to right
        # also both nums1 and nums2 are non decreasing, so if nums2[j] < nums1[i] and we swap them - we cannot have a fixed relation between nums2[j] and nums[j+1] and nums1[i+1] - the monotonicity is lost
        # example: nums1 = [4, 5, 6, 0, 0, 0], nums2 = [1, 2, 3]
        # swap 4 and 1, nums1 = [1, 5, 6, 0, 0, 0], nums2 = [4, 2, 3]
        # now we cannot say as a rule if 2 < 5 or 4 < 5
        # so we cannot start from left
        
        # we already have auxillary space in nums1, so we can start from right end of nums1 and keep filling the elements from right end
        
        i = m - 1 # nums1 range from 0 to m-1
        j = n - 1 # nums2 prefilled values range from 0 to n-1
        k = m + n - 1 # nums1 range from 0 to m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:   
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        



sol = Solution()
sol.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
