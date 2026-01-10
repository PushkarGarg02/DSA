# Merging Overlapping Intervals

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

## Example 1
- **Intervals:** `[[1,4], [2,5], [7,9]]`
- **Output:** `[[1,5], [7,9]]`
- **Explanation:** The first two intervals `[1,4]` and `[2,5]` overlap, so they are merged into one `[1,5]`.

## Example 2
- **Intervals:** `[[6,7], [2,4], [5,9]]`
- **Output:** `[[2,4], [5,9]]`
- **Explanation:** The intervals `[6,7]` and `[5,9]` overlap, so they are merged into one `[5,9]`.

## Example 3
- **Intervals:** `[[1,4], [2,6], [3,5]]`
- **Output:** `[[1,6]]`
- **Explanation:** All the given intervals overlap, so they are merged into a single interval.

## Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start(i) <= end(i) <= 10^4