# https://leetcode.com/problems/is-subsequence
#   What is subsequence and subString?
#   Subsequence: a sequence that appears in the same relative order, but not necessarily contiguous.
#   SubString: a contiguous sequence of symbols that appears in the same relative order as the original string.


class Solution:
    # my soln
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if not s:
            return True
        # following is useless as next while + if doing same thing
        # while j < len(t) and s[i] != s[j]:
        #     j += 1
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            # below or you can combine the two returs as per 2nd soln
            if i == len(s):
                return True
            j += 1
        return False

    # from https://leetcode.com/problems/is-subsequence/solutions/1811508/python-javascript-easy-solution-with-very-clear-explanation/comments/1411952
    def isSubsequence2(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


sol = Solution()
sol.isSubsequence("axc", "ahbgdc")
