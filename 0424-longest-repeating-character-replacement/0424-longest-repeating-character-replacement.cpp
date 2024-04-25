class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> window;
        int l = 0, res = 0, maxFreq = 0;

        for (int r = 0; r < s.size(); ++r) {
            window[s[r]]++;
            maxFreq = max(maxFreq, window[s[r]]);

            while (r - l + 1 - maxFreq > k) {
                window[s[l]]--;
                if (window[s[l]] == 0) {
                    window.erase(s[l]);
                }
                l++;
            }

            res = max(res, r - l + 1);
        }

        return res;
    }
};