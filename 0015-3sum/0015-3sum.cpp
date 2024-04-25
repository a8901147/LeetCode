class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int index=0; index<nums.size()-2; index++) {
            if (nums[index]>0) {
                break;
            }

            if (index>0 and nums[index] == nums[index-1]){
                continue;
            }

            int left = index + 1;
            int right = nums.size()-1;

            while (left<right){
                int threesum = nums[index] + nums[left] + nums[right];
                if (threesum==0) {
                    res.push_back({nums[index],nums[left],nums[right]});
                    left += 1;
                    right -= 1;
                    while (left < right and nums[left] == nums[left - 1])
                        left += 1;
                }
                else if (threesum>0){
                    right -= 1;
                }
                else{
                    left += 1;
                }
            }
        }
        return res;
    }
};