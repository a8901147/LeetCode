class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int sell_max = 0;
        for (int i=prices.size()-1; i>-1; i--) {
            if (sell_max - prices[i]>0) {
                res = max(res, sell_max-prices[i]);
            }
            sell_max = max(sell_max, prices[i]);
        }
        return res;
    }
};