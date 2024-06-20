class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        d = dict()
        result = 0
        left = 0
        for right in range(len(s)):
            if s[right] in d:
                left = max(left, d[s[right]] + 1)

            d[s[right]] = right
            result = max(result, right - left + 1)

        return result


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
