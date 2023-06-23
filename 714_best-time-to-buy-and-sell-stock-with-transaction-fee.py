"""
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pos = -prices[0]
        profit = 0
        for i in range(1, len(prices)):
            pos = max(pos, profit - prices[i])
            profit = max(profit, pos + prices[i] - fee)

        return profit


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    sol = Solution()
    result = sol.maxProfit(prices, fee)
    print(result)
