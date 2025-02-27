class Solution:
    def longestPalindrome(self, s: str) -> str:
        # m, n = 0, len(s) - 1
        m = 0
        n = len(s) - 1
        while m < n:
            if self.isPalindrome(s, m, n):
                return s[m:n]
            m += 1
            n -= 1

        return s[0]

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


sol = Solution()
sol.longestPalindrome("babad")
