int minCostClimbingStairs(int* cost, int costSize) {
    int min_cost[costSize];
    min_cost[0] = cost[0];
    min_cost[1] = cost[1];
    for (int i = 2; i<costSize; i++){
        min_cost[i] = fmin(min_cost[i-1],min_cost[i-2])+cost[i];
    }

    return fmin(min_cost[costSize-1],min_cost[costSize-2]);
}