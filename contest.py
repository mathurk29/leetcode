# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

from typing import List


def calculateTax(brackets: List[List[int]], income: int) -> float:
    ans = prev = 0
    for hi, pct in brackets:
        hi = min(hi, income)
        ans += (hi - prev)*pct/100
        prev = hi
    return ans


calculateTax()
