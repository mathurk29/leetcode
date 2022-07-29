class Solution:

    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.expandPalindrome(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            # even case, like "abba"
            tmp = self.expandPalindrome(s, i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer

    def expandPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
