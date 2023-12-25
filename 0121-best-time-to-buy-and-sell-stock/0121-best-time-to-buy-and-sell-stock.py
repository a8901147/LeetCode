class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMaxSell=0
        res = 0
        for index in range(len(prices)-1,-1,-1):
            res=max(curMaxSell-prices[index],res) if curMaxSell-prices[index] else res
            curMaxSell=max(prices[index],curMaxSell) 
        return res