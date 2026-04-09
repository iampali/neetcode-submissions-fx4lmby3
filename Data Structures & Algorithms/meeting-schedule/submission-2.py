"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start )
        last_end = None
        for i in intervals:
            if not last_end:
                last_end = i.end
                continue
            
            if i.start < last_end:
                return False

            last_end = i.end

        return True
