# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize the minimum price as infinity
        max_profit = 0  # Initialize the maximum profit as 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if current profit is higher

        return max_profit