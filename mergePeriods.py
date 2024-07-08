class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return intervals

        intervals.sort(key=lambda i: i[0])

        no_intervals = [intervals[0]]

        for i in intervals[1:]:
            last_i = no_intervals[-1]
            if i[0] <= last_i[1]:
                last_i[1] = max(last_i[1], i[1])
            else:
                no_intervals.append(i)

        return no_intervals
