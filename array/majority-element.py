# https://leetcode.com/problems/majority-element/submissions/
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = defaultdict(lambda: 0)
        for x in nums:
            cache[x] += 1
            if cache[x] > len(nums) / 2:
                return x

# refer https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
# http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
