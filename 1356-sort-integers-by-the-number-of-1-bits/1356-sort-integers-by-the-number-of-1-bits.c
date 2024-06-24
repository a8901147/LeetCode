/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int findweight(int num){
    int res = 0;

    while (num){
        res += 1;
        num &= (num-1);
    }

    return res;
}

int compare(const void* a, const void* b){
    int num1 = *(int*)a;
    int num2 = *(int*)b;

    int weight1 = findweight(num1);
    int weight2 = findweight(num2);

    if (weight1 == weight2) {
        return (num1 - num2);
    }
    return (weight1 - weight2);
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    int* sortArr = (int*)malloc(sizeof(int)*arrSize);
    sortArr = arr;

    qsort(sortArr,arrSize,sizeof(int),compare);

    *returnSize = arrSize;
    return sortArr;
}