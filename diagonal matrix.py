# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        try:
            for i, row in enumerate(grid):
                for j, col in enumerate(row):
                    if i == j or i + j == len(grid) - 1:  # diagonal element
                        if col == 0:
                            raise StopIteration
                    else:  # non - diagonal elem
                        if col is not 0:
                            raise StopIteration
        except StopIteration:
            return False
        return True


grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]

sol = Solution()
sol.checkXMatrix(grid)

grid = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]
sol.checkXMatrix(grid)
