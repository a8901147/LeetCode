class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        backtrack(0,nums);
        return res;
    }

private:
    vector<vector<int>> res;
    vector<int> part;
    void backtrack(int cur,vector<int>& nums){
        if (cur == nums.size()) {
            res.push_back(part);
            return;
        }
        
        // Include the current element
        part.push_back(nums[cur]);
        backtrack(cur + 1, nums);
        part.pop_back();
        
        // Skip duplicates
        while (cur + 1 < nums.size() && nums[cur] == nums[cur + 1]) {
            cur++;
        }
        
        // Exclude the current element and proceed
        backtrack(cur + 1, nums);
    }
};