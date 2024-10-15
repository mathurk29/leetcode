# https://leetcode.com/problems/determine-if-two-strings-are-close

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        # Op 1 tells letters positions can be swapped -
        # thus order not imp -
        # thus only letters should be same.
        if c1.keys() != c2.keys():
            return False

        # Op 2 enables you to interchange freq of alphabets -
        # thus all freq in first word and second word should be same
        return sorted(c1.values()) == sorted(
            c2.values()
        )  # I used set which caused false positive


word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"


sol = Solution()
sol.closeStrings(word1, word2)
