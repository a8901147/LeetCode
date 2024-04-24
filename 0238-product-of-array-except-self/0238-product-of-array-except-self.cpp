class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();

        vector<int> post_prod(length,1);
        int post = 1;
        for (int i = length-1; i>=0; i--){
            post_prod[i] = post;
            post *= nums[i];
        }

        vector<int> res;
        int prev = 1;
        for (int i = 0; i < length; ++i) {
            res.push_back(post_prod[i] * prev);
            prev *= nums[i];
        }

        return res;
    }
};