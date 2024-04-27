class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<pair<int,int>> window;

        for (int r = 0; r<nums.size(); r++) {
            int cur = nums[r];

            if (!window.empty() && r-window[0].first==k) {
                window.pop_front();
            }

            while (!window.empty() && window.back().second <= cur) {
                window.pop_back();
            }
            window.push_back({r,cur});

            if (r >= k-1){
                res.push_back(window[0].second);
            }
        }
        return res;
    }
};