int findDuplicate(int* nums, int numsSize) {
    //numsSize = sizeof(nums) / sizeof(nums[0]);
    int *cache = (int *)calloc(numsSize,sizeof(int));
    int num;
    int res;

    for (int i = 0; i<numsSize; i++){
        num = nums[i];

        if (cache[num]){
            free(cache);
            res = num;
            break;
        }
        cache[num] = 1;
    }
    return res;
}