class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def print_interval(i):
    print("["+ str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            return intervals.append(new_interval)

        merged_intervals = []
        i = 0

        while i < len(intervals) and intervals[i].end < new_interval.start:
            merged_intervals.append(intervals[i])
            i += 1

        while i < len(intervals) and new_interval.end >= intervals[i].start:
            new_interval.start = min(new_interval.start,intervals[i].start)
            new_interval.end = max(new_interval.end, intervals[i].end)
            i += 1

        merged_intervals.append(new_interval)

        while i < len(intervals):
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals

def main():
    sol = Solution()
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    print("Intervals after inserting the new interval: ",end="")
    for i in (sol.insert(intervals, Interval(4, 6))):
        print_interval(i)
    print()

    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    print("Intervals after inserting the new interval: ",end="")
    for i in (sol.insert(intervals, Interval(4, 10))):
        print_interval(i)
    print()

    intervals = [Interval(2, 3), Interval(5, 7)]
    print("Intervals after inserting the new interval: ",end="")
    for i in (sol.insert(intervals, Interval(1, 4))):
        print_interval(i)
    print()

main()