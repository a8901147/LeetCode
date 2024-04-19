class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, int> dict_s;
        std::unordered_map<char, int> dict_t;

        // Counting characters in string s
        for (char c : s) {
            dict_s[c]++;
        }

        // Counting characters in string t
        for (char c : t) {
            dict_t[c]++;
        }

        // Comparing both dictionaries
        if (dict_s == dict_t) {
            return true;
        }

        return false;
        }
};