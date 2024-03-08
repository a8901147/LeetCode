class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int end = intervals.size();
        if (end==1){
            return 0;
        }
        sort(intervals.begin(), intervals.end());
        int res = 0;
        int prev_tail = intervals[0][1];
        for (int i = 1; i < end; i++){
            if (prev_tail <= intervals[i][0]){
                prev_tail = intervals[i][1];
                continue;
            }
            prev_tail = min(prev_tail, intervals[i][1]);
            res += 1;
        }
        return res;
    }
};