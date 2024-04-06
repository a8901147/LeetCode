class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] < start:
                res.append([start,end])
                continue
            
            prev_start, prev_end = res.pop()
            res.append([prev_start,max(prev_end,end)])

        return res

        