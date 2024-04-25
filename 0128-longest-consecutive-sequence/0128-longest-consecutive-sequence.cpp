class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        unordered_set<int> numSet(nums.begin(), nums.end());
        vector<int> nums_no_repeated(numSet.begin(), numSet.end());
        sort(nums_no_repeated.begin(), nums_no_repeated.end());

        int res = 0;
        int counter = 1;

        for (int i = 0; i < nums_no_repeated.size(); i++) {
            if (i-1>=0 and nums_no_repeated[i] == nums_no_repeated[i - 1] + 1) {
                counter += 1;
            } else {
                counter = 1;
            }
            res = max(res, counter);
        }

        return res;
    }
};