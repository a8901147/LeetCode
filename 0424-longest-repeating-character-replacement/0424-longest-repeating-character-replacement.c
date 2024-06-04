int findmax(int arr[]){
    int max = arr[0];
    for(int i = 0; i<26; i++){
        if (arr[i]>max){
            max = arr[i];
        }
    }
    return max;
}

int characterReplacement(char* s, int k) {
    int map[26] = {0};
    int length = strlen(s);
    int l = 0;
    int res = 0;

    for(int r = 0; r<length; r++){
        int index = s[r]-'A';
        map[index] += 1;
        
        // r-l+1 = cur_length
        if (r-l+1-findmax(map)>k){
            map[(int)s[l]-'A'] -= 1;
            l += 1;
        }

        res = fmax(res, r-l+1);
    }
    return res;
}