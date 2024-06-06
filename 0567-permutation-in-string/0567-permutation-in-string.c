bool compare_map(char s1_arr[], char s2_arr[]){
    for (int i = 0; i<26; i++){
        if (s1_arr[i] != s2_arr[i]){
            return false;
        }
    }
    return true;
}

bool checkInclusion(char* s1, char* s2) {
    if (strlen(s1)>strlen(s2)){
        return false;
    }

    char s1_map[26] = {0};
    char s2_map[26] = {0};

    for (int i = 0; i<strlen(s1); i++){
        s1_map[s1[i]-'a'] += 1;
        s2_map[s2[i]-'a'] += 1;
    }

    if (compare_map(s1_map,s2_map)){
        return true;
    }

    for (int i = strlen(s1); i<strlen(s2); i++){
        s2_map[s2[i]-'a'] += 1;
        s2_map[s2[i-strlen(s1)]-'a'] -= 1;

        if (compare_map(s1_map,s2_map)){
            return true;
        }
    }
    return false;
}