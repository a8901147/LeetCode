class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        int size = intervals.size();
        if (size <= 1){
            return true;
        }
        sort(intervals.begin(),intervals.end());

        int prev_end = intervals[0][1];
        for (int i=1; i<intervals.size(); i++){
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start < prev_end) {
                return false;
            }
            prev_end = end;
        }
        return true;
    }
};