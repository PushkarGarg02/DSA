class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def print_interval(i):
    print("["+ str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def find_intersection(self, intervals_a, intervals_b):
        interval_intersection = []
        i, j = 0, 0

        while i < len(intervals_a) and j < len(intervals_b):
            a_overlaps_b = (intervals_a[i].start >= intervals_b[j].start) and (intervals_a[i].start <= intervals_b[j].end)
            b_overlaps_a = (intervals_a[i].start <= intervals_b[j].start) and (intervals_a[i].end >= intervals_b[j].start)

            if a_overlaps_b or b_overlaps_a:
                start = max(intervals_a[i].start, intervals_b[j].start)
                end = min(intervals_a[i].end, intervals_b[j].end)
                interval_intersection.append(Interval(start,end))

            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1

        return interval_intersection


def main():
    sol = Solution()
    intervals_a = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    intervals_b = [Interval(2, 3), Interval(5, 7)]
    print("Intervals Intersection: ", end="")
    for i in sol.find_intersection(intervals_a,intervals_b):
        print_interval(i)


    intervals_a = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
    intervals_b = [Interval(5, 10)]
    print("Intervals Intersection: ", end="")
    for i in sol.find_intersection(intervals_a,intervals_b):
        print_interval(i)

main()