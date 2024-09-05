from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])


testcases = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
sol = Solution()
for testcase in testcases:
    sol.minCostClimbingStairs(testcase)
