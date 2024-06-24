char* toHex(int num) {
    char* res = (char*)malloc(sizeof(char)*9);
    res[8] = '\0';
    if (num==0){
        res[7] = '0';
        return res+7;
    }
    
    unsigned int n = num;
    int index = 7;
    char hextochar[] = "0123456789abcdef";
    while (n){
        res[index--] = hextochar[n%16];
        n /= 16;
    }
    return res + index + 1;
}