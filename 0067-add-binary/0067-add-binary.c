char* addBinary(char* a, char* b) {
    int a_len = strlen(a);
    int b_len = strlen(b);
    int max_len = a_len > b_len ? a_len : b_len;
    char* result = (char*)malloc(sizeof(char) * (max_len + 2));
    int carry = 0;

    result[max_len + 1] = '\0'; // Null-terminate the string

    for (int i = a_len - 1, j = b_len - 1, k = max_len; i >= 0 || j >= 0; --i, --j, --k) {
        int sum = carry;
        if (i >= 0) sum += a[i] - '0';
        if (j >= 0) sum += b[j] - '0';
        result[k] = (sum % 2) + '0';
        carry = sum / 2;
    }
    
    if (carry) {
        result[0] = '1';
        return result;
    } else {
        return result+1; // Return the adjusted result
    }
}