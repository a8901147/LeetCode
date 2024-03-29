class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        res = 0
        for price in prices:
            res = max(res,price-cur_min)
            cur_min = min(cur_min,price)
        return res
