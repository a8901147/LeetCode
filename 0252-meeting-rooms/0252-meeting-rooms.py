class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        prev_end = -1
        for start, end in intervals:
            if start < prev_end:
                return False
            prev_end = end
        return True