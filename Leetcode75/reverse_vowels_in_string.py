# https://leetcode.com/problems/reverse-vowels-of-a-string


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


sol = Solution()
assert sol.reverseVowels("leetcode") == "leotcede"
