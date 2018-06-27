"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

[15,18] [8,10] [2,6] [1,3]
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + ',' + str(self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, cmp=lambda x,y: cmp(x.start, y.start), reverse=True)
        num = len(intervals)
        for i in range(num-1, 0, -1):
            item = intervals[i]
            if item.end >= intervals[i-1].start:
                intervals[i-1].start = item.start
                intervals[i-1].end = max(intervals[i-1].end, item.end)
                intervals.pop(i)
        intervals.reverse()
        return intervals

    def merge_2(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda x: x.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)
        return out


params = []
for item in [[1,6],[5,6],[8,10],[9,18]]:
    params.append(Interval(item[0], item[1]))
res = Solution().merge_2(params)
for i in res:
    print i