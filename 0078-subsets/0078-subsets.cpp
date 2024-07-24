class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        backtrack(0,nums);
    
        return res;
    }

private:
    vector<vector<int>> res;
    vector<int> part;
    void backtrack(int cur,vector<int>& nums){
        if (cur==nums.size()){
            res.push_back(part);
            return;
        }
        part.push_back(nums[cur]);
        backtrack(cur+1,nums);
        part.pop_back();
        backtrack(cur+1,nums);
    }
};