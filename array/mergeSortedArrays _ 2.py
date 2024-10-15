# Bad complexity O(mn)


from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        merged = []

        i = j = 0

        m = len(nums1)
        n = len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums2[j:])
        merged.extend(nums1[i:])

        if (m + n) % 2 == 0:
            median = (
                merged[(m + n - 1) // 2] + merged[(m + n - 1) // 2 + 1]
            ) / 2
        else:
            median = merged[(m + n) // 2]

        return median


sol = Solution()

nums1 = [1, 2]
nums2 = [3, 4]

sol.findMedianSortedArrays(nums1, nums1)
