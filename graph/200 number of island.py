from typing import List


class Solution:

    def __init__(self):
        self.m = None
        self.n = None
        self.grid = None
        self.result = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == "1":
                    self.result += 1
                    self.dfs(row, col)
        return self.result

    def dfs(self, i, j):
        while 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j] == "1":
            self.grid[i][j] = "0"
            self.dfs(i + 1, j)
            self.dfs(i, j + 1)
            self.dfs(i - 1, j)
            self.dfs(i, j - 1)


sol = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
sol.numIslands(grid2)
