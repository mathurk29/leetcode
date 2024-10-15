# https://leetcode.com/problems/non-overlapping-intervals

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        left, right = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            remove = False
            if left < interval[0]:
                left = interval[0]
                remove = True
            if interval[1] > right:
                remove = True
                right = interval[1]
            if remove:
                result += 1
        return result
