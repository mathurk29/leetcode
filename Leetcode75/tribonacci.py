class Solution:
    # def tribonacci(self, n: int) -> int:
    #     l = list()
    #     l.extend([0,1,1])
    #     for i in range(3,n+1):
    #         l.extend([l[i-1] + l[i-2] + l[i-3]])
    #     return l[i]

    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n):
            dp[i % 3] = sum(dp)
        return dp[n % 3]


sol = Solution()
sol.tribonacci(4)
