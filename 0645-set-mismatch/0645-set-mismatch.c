/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    *returnSize = 2;
    int* res = (int*)malloc(sizeof(int)*2); //[duplicate,missing]
    int* cache = (int*)calloc(numsSize+1,sizeof(int));

    int total = (1+numsSize)*numsSize/2;
    int cur;
    for (int i = 0; i<numsSize; i++){
        cur = nums[i];
        if (cache[cur]){
            res[0] = cur;
            continue;
        }
        cache[cur] = 1;
        total -= cur;
    }
    free(cache);
    res[1] = total;
    return res;
}