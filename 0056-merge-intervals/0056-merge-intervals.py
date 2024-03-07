class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_tail = res[-1][1]
            if prev_tail < start:
                res.append([start,end])
            else:
                res[-1][1] = max(end,prev_tail)

        return res
