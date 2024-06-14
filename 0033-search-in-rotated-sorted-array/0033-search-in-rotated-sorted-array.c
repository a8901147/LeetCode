int search(int* nums, int numsSize, int target) {
    int l = 0;
    int r = numsSize - 1;
    int middle;

    while (l <= r) {
        middle = l + (r - l) / 2; // This avoids potential overflow compared to (l + r) / 2
        if (nums[middle] == target) {
            return middle;
        }

        // Check if the left side is sorted
        if (nums[l] <= nums[middle]) {
            // Target is in the left sorted part
            if (nums[l] <= target && target < nums[middle]) {
                r = middle - 1;
            } else {
                l = middle + 1;
            }
        } 
        // The right side must be sorted
        else {
            // Target is in the right sorted part
            if (nums[middle] < target && target <= nums[r]) {
                l = middle + 1;
            } else {
                r = middle - 1;
            }
        }
    }
    return -1; // Target not found
}
