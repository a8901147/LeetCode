class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_tail = intervals[0][1]
        for start, end in intervals[1:]:
            if prev_tail <= start:
                prev_tail = end
                continue

            prev_tail = min(prev_tail,end)
            res += 1
        return res
            