class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;

        int res = 0;
        while (l<r) {
            int area = (r-l)*min(height[l],height[r]);
            res = max(res, area);
            if (height[l] < height[r]) {
                l += 1;
            }
            else{
                r -= 1;
            }
        }
        return res;
    }
};