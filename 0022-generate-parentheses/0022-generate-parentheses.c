/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void backtracking(char* part, int left_count, int right_count, int n, char** res, int* returnSize) {
    if (left_count == n && right_count == n){
        res[*returnSize] = (char*)malloc((2 * n + 1)*sizeof(char));
        strcpy(res[(*returnSize)++],part);
        return;
    }

    if (left_count < n) {
        strcat(part, "(");
        backtracking(part, left_count + 1, right_count, n, res, returnSize);
        part[strlen(part) - 1] = '\0';
    }
    if (right_count < n && right_count < left_count) {
        strcat(part, ")");
        backtracking(part, left_count, right_count + 1, n, res, returnSize);
        part[strlen(part) - 1] = '\0';
    }
}

char** generateParenthesis(int n, int* returnSize) {
    char** res = (char**)malloc(sizeof(char*)*1430);
    char* part = (char*)malloc(sizeof(char)*(2*n+1));
    part[0] = '\0';
    *returnSize = 0;
    backtracking(part, 0, 0, n, res, returnSize);
    free(part);
    return res;
}