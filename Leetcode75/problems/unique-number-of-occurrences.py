# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for item in arr:
            d[item] += 1

        occurences = list(d.values())
        return len(occurences) == len(set(occurences))
