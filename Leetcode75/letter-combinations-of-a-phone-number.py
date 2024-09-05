from typing import List
import itertools

phone_dict = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = list()
        for d in digits:
            digit_to_letters.append(phone_dict[int(d)])
        return list(itertools.product(digit_to_letters))
        return list(zip([[item] for item in digit_to_letters]))


sol = Solution()
sol.letterCombinations("23")
