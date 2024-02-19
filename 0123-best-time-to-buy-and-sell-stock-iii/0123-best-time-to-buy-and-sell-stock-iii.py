class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_profits = []
        cur_min = prices[0]
        max_profit_so_far = 0
        for price in prices:
            max_profit_so_far = max(max_profit_so_far, price-cur_min)
            left_profits.append(max_profit_so_far)
            cur_min = min(cur_min,price)

        right_profits = [0]*len(prices)
        cur_max = prices[-1]
        max_profit_so_far = 0
        for i in range(len(prices)-1,-1,-1):
            price = prices[i]
            max_profit_so_far = max(max_profit_so_far, cur_max-price)
            right_profits[i] = max_profit_so_far
            cur_max = max(cur_max,price)

        res = 0
        for i in range(len(prices)):
            res = max(res,left_profits[i]+right_profits[i])
        return res