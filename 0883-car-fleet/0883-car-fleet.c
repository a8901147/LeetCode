int compare(const void *a, const void *b) {
    return ((int *)b)[0] - ((int *)a)[0];
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    int (*pos_index)[2] = malloc(positionSize * 2 * sizeof(int));
    for (int i = 0; i < positionSize; i++) {
        pos_index[i][0] = position[i];
        pos_index[i][1] = speed[i];
    }

    qsort(pos_index, positionSize, 2*sizeof(int), compare);

    double *stack = (double *)malloc(positionSize * sizeof(double));
    int stackSize = 0;

    for (int i = 0; i < positionSize; i++) {
        int pos = pos_index[i][0];
        int spd = pos_index[i][1];
        int travel_dis = target - pos;
        double travel_time = (double)travel_dis / spd;

        if (stackSize == 0 || travel_time > stack[stackSize - 1]) {
            stack[stackSize++] = travel_time;
        }
    }

    free(pos_index);
    free(stack);

    return stackSize;
}

