# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            # we can return the first occurence where value is greater than remaining number of elements
            if n - i <= v:
                return n - i
        return 0

inputs = [
    ([0],0),
    ([1],1),
    ([2], 1),
    ([0,1],1),
    ([1,1], 1),
    ([1,1,1], 1),
    ([1,2,3], 2),
    ([3,2,1],2),
    ([1,0],1),
    ([100],1),
    ([0,0,2],1)
]

for input,expected in inputs:
    assert (result := Solution().hIndex(input)) == expected, f"for input {input} -> expected {expected} but got {result}"