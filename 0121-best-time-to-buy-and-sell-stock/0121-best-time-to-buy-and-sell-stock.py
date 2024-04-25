class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        sell_max = 0
        for price in reversed(prices):
            if sell_max - price > 0:
                res = max(res, sell_max - price)
            sell_max = max(sell_max,price)

        return res
        