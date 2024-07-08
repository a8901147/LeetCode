int sumIndicesWithKSetBits(int* nums, int numsSize, int k){
    int res = 0;
    for(int i=0; i<numsSize; i++){
        int cur = i;
        int nums_1 = 0;
        while(cur){
            nums_1 += cur & 1;
            cur = cur >> 1;
        }

        if(nums_1==k){
            res += nums[i];
        }
    }
    return res;
}