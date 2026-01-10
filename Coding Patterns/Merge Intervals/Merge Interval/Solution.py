class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def print_interval(i):
    print("["+ str(i.start) + ", " + str(i.end) + "]", end='')

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        #sort the intervals
        intervals.sort(key=lambda obj: obj.start)

        mergedIntervals = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end: # overlap confirmed
                end = max(interval.end,end)
            else:
                mergedIntervals.append(Interval(start,end)) #insert the interval before starting a new start and end
                start = interval.start  # set new start for next iteration
                end = interval.end      # set new end for next iteration

        mergedIntervals.append(Interval(start,end)) #insert last interval
        return mergedIntervals

def main():
    sol = Solution()
    print("Merged Intervals: ", end='')
    for i in sol.merge([Interval(1,4),Interval(2,5),Interval(7,9)]):
        print_interval(i)
    print()

    print("Merged intervals: ", end='')
    for i in sol.merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        print_interval(i)
    print()

    print("Merged intervals: ", end='')
    for i in sol.merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        print_interval(i)
    print()



main()



