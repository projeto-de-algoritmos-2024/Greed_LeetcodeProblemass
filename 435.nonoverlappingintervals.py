class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        intervals.sort()
        removed = 0

        first_end = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= first_end: first_end = e
            else: 
                removed += 1
                first_end = min(e, first_end)
        
        return removed
