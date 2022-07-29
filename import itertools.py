import itertools


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        if num == 0:
            return 0

        base = [k + i * (10 ** 1) for i in range(10)]

        for i in range(1, len(base)+1):
            result = itertools.combinations(base*i, i)
            for x in list(result):
                if sum(x) == num:
                    return len(x)

        return -1


sol = Solution()
sol.minimumNumbers(37, 2)
