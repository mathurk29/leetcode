# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            # nums1 = nums2 is not in-place. The memory loc reference by num1 isn't changed but nums1 started pointing to nums2 loc
            nums1[:] = nums2[:]
            return
        if n == 0:
            return

        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        if j >= 0:
            nums1[:j+1] = nums2[:j+1]

        print(f"nums1 is {nums1}")


sol = Solution()
sol.merge([2, 0],
          1,
          [1],
          1)


# refer for better sol  = https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
