# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:

    def generate(self, numRows):
        res = [[1]]
        for _ in range(2, numRows + 1):  # 2nd row to last row
            res.append(
                list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
            )
        return res[:numRows]


sol = Solution()
sol.generate(5)
