/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize) {
    int* arr = (int*)malloc((encodedSize+1)*sizeof(int));
    arr[0] = first;
    for(int i=1; i<encodedSize+1; i++){
        arr[i] = arr[i-1]^encoded[i-1];
    }
    * returnSize = encodedSize+1;
    return arr;
}