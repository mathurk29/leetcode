from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            smaller_height = min(height[left], height[right])
            area = width * smaller_height

            result = max(result, area)

            while height[left] > height[left + 1] and left < right:
                left += 1
            while height[right] > height[right - 1]:
                right -= 1

        return result


sol = Solution()


sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
