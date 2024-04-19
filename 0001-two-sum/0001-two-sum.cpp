class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;

        for (int i = 0; i < nums.size(); ++i) {
            
            if (hashmap.find(nums[i])!=hashmap.end()){
                return {i, hashmap[nums[i]]};
            }

            int complement = target - nums[i];
            hashmap[complement] = i;
        }
        return {};
    }
};