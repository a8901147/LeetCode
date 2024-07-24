class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> part;
        vector<bool> used(nums.size(), false);
        backtrack(nums, used, part, res);
        return res;
    }

private:
    void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& part, vector<vector<int>>& res) {
        if (part.size() == nums.size()) {
            res.push_back(part);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;

            part.push_back(nums[i]);
            used[i] = true;
            backtrack(nums, used, part, res);
            part.pop_back();
            used[i] = false;
        }
    }
};