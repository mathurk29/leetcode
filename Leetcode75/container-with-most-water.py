# https://leetcode.com/problems/container-with-most-water/description/


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_so_far = 0
        # Since the height of container is limited by the smaller edge
        # so discard the higher edge in next iteration.
        # i.e. move pointer towards the samller edge
        while i < j:
            max_so_far = max(max_so_far, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_so_far
