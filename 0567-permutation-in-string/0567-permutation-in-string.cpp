class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size()>s2.size()){
            return false;
        }
        
        unordered_map<char,int> s1_map;
        for (char c : s1) {
            s1_map[c]++;
        }

        unordered_map<char,int> s2_map;
        for (int i=0; i<s1.size(); i++) {
            char c = s2[i];
            s2_map[c]++;
        }
        
        if (s2_map == s1_map){
            return true;
        }

        for (int i=s1.size(); i<s2.size(); i++ ){
            s2_map[s2[i]] ++;
            s2_map[s2[i-s1.size()]] --;
            if (s2_map[s2[i-s1.size()]]==0){
                s2_map.erase(s2[i-s1.size()]);
            }
            if (s2_map == s1_map){
                return true;
            }
        }
        return false;
    }
};