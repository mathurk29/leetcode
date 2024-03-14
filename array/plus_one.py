
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        right = len(digits) - 1

        if digits[right] < 9:
            digits[right] += 1
            return digits
        else:
            while digits[right] == 9:
                digits[right] = 0
                right -= 1
                if right == -1:
                    digits.insert(0, 0)
                    right += 1
            digits[right] += 1
            return digits


sol = Solution()
sol.plusOne(digits=[9, 9, 9, 9])
