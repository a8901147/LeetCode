class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(index,canBuy):
            if index >= len(prices):
                return 0
            if (index,canBuy) in dp:
                return dp[(index,canBuy)]


            if canBuy:
                buy = dfs(index+1,False) - prices[index]
                cool = dfs(index+1,True)
                dp[(index,canBuy)] = max(buy,cool)
            else:
                sell = dfs(index+2,True) + prices[index]
                cool = dfs(index+1,False)
                dp[(index,canBuy)] = max(sell,cool)
            return dp[(index,canBuy)]

        return dfs(0,True)