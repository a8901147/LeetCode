class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int,vector<int>,greater<int>> pq;

        int res = 0;
        for (int i=0; i<intervals.size(); i++){
            int start = intervals[i][0];
            int end = intervals[i][1];

            while (pq.size() && start >= pq.top()){
                pq.pop();
            }
            pq.push(end);

            int cur_size = pq.size();
            res = max(res,cur_size);
        }
        return res;
    }
};