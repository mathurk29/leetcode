# https://leetcode.com/problems/majority-element/

from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = len(nums) // 2
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return max(counter, key=counter.get)


    def mooreVotingAlgo(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly
        '''
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate