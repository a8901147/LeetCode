/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* orArray(int* nums, int numsSize, int* returnSize) {
    int* res = (int*)calloc(numsSize-1, sizeof(int));
    for (int i = 0; i<numsSize-1; i++){
        res[i] = nums[i] | nums[i+1];
        //res += 1;
    }
    * returnSize = numsSize-1;
    return res;
}