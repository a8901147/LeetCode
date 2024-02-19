class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, can_buy, cur_sum):
            if i == len(prices):
                return 0
            
            if (i,can_buy) in memo:
                return memo[(i,can_buy)]
            
            if can_buy:
                buy = dfs(i+1, False, cur_sum)-prices[i]
                cool = dfs(i+1, True, cur_sum)
                memo[(i,can_buy)] = max(buy,cool)
                return memo[(i,can_buy)]
            else:
                sell = dfs(i+1, True, cur_sum)+prices[i]
                cool = dfs(i+1, False, cur_sum)
                memo[(i,can_buy)] = max(sell,cool)
                return memo[(i,can_buy)]

        return dfs(0,True,0)