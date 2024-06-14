int findMin(int* nums, int numsSize) {
    int l = 0;
    int r = numsSize-1;
    int middle;
    while (l<r){
        if (nums[l]<nums[r]){
            return nums[l];
        }

        middle = (l+r)/2;
        if (nums[middle]<nums[r]){
            r = middle;
        }
        else{
            l = middle+1;
        }
    }
    return nums[l];
}