char* minWindow(char* s, char* t) {
    if (strlen(s)<strlen(t)){
        return "";
    }

    int to_do_task = 0;

    int t_map[128] = {0};
    for(int i = 0; i<strlen(t); i++){
        t_map[t[i]] += 1;
        if (t_map[t[i]] ==1 ){
            to_do_task += 1;
        }
    }

    int l = 0;
    int s_map[128] = {0};
    int min_len = strlen(s)+1;
    int min[2] = {0,0};
    for (int r = 0; r<strlen(s); r++){
        s_map[s[r]] += 1;

        if (s_map[s[r]] == t_map[s[r]]){
            to_do_task -= 1;
        }

        if (to_do_task!=0){
            continue;
        }

        while (to_do_task==0){
            if (r-l+1<min_len){
                min_len = r-l+1;
                min[0] = l;
                min[1] = r;
            }

            s_map[s[l]] -= 1;
            if (t_map[s[l]]-s_map[s[l]]==1){
                to_do_task += 1;
            }
            l += 1;
        }
    }

    if (min_len == strlen(s)+1){
        return "";
    }
    char* res = (char*)malloc(sizeof(char)*(min_len+1));
    strncpy(res, s+min[0], min_len);
    res[min_len] = '\0';
    return res;
}