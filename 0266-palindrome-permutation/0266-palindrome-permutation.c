bool canPermutePalindrome(char* s) {
    int alpha[26] = {0};
    for (int i = 0; i<strlen(s); i++){
        alpha[s[i]-'a'] ^= 1;
    }

    int counter = 0;
    for (int i = 0; i<26; i++){ 
        if (alpha[i]){
            counter++;
        }

        if (counter>1){
            return false;
        }
    }
    return true;
}