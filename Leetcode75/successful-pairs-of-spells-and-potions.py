# https://leetcode.com/problems/successful-pairs-of-spells-and-potions


from typing import List
import bisect


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        return [
            len(potions)
            - bisect.bisect_left(potions, (success + spell - 1) // spell)
            for spell in spells
        ]


sol = Solution()

assert sol.successfulPairs(
    spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7
) == [
    4,
    0,
    3,
]


# bisect left algo:


def bisect_left_gpt(self, nums, x):
    """
    Locate the insertion point for x in a to maintain sorted order.
    The parameters lo and hi may be used to specify a subsequence of the list.
    Returns the leftmost place in the list to insert x.
    """
    if hi is None:
        hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Example usage:
sorted_list = [1, 3, 4, 4, 5, 8, 9]
value_to_insert = 4
index = bisect_left_gpt(sorted_list, value_to_insert)
print(f"The leftmost insertion point for {value_to_insert} is at index {index}")
