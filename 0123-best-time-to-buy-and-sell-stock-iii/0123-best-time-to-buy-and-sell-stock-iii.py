class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        memo = {}
        def dfs(i, cur_sum, can_buy, transaction):
            if transaction == 0 or i==len(prices):
                return 0
            if (i,can_buy,transaction) in memo:
                return memo[(i,can_buy,transaction)]
            
            if can_buy:
                buy = dfs(i+1, cur_sum, False, transaction) - prices[i]
                cool = dfs(i+1, cur_sum, True, transaction)
                memo[(i,can_buy,transaction)] = max(buy,cool)
                return memo[(i,can_buy,transaction)]
            else:
                sell = dfs(i+1, cur_sum, True, transaction-1) + prices[i]
                cool = dfs(i+1, cur_sum, False, transaction)
                memo[(i,can_buy,transaction)] = max(sell,cool)
                return memo[(i,can_buy,transaction)]

        return dfs(0,0,True,2)