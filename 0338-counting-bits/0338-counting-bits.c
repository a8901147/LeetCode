/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int* res = (int*)malloc((n+1)*sizeof(int));
    for(int i=0; i<n+1; i++){
        int num = i;
        int counter = 0;
        while(num){
            counter += num&1;
            num = num>>1;
        }
        res[i] = counter;
    }
    *returnSize = n+1;
    return res;
}