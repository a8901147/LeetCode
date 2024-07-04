int coinChange(int* coins, int coinsSize, int amount) {
    int* amounts = (int*)calloc(amount+1,sizeof(int));
    for (int i = 0; i<amount+1; i++){
        amounts[i] = INT_MAX;
    }
    amounts[0] = 0;

    for (int cur = 1; cur<amount+1; cur++){
        int min = 0;
        for (int coin_index = 0; coin_index<coinsSize; coin_index++){
            int coin = coins[coin_index];
            if (cur - coin >= 0 && amounts[cur - coin] != INT_MAX) {
                if (amounts[cur] > amounts[cur - coin] + 1) {
                    amounts[cur] = amounts[cur - coin] + 1;
                }
            }
        }
    }

    int res = amounts[amount] == INT_MAX ? -1 : amounts[amount];
    free(amounts);
    return res;
}