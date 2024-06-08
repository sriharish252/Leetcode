from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # Sort and compare adjacent values, greedily keep the interval with the lesser end
    #   In other words, greedily remove the longer interval, so that minimum intervals are removed
    count = 0
    intervals.sort()
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            count += 1
            prevEnd = min(prevEnd, end)
    return count

# Time Complexity - O(n*logn) => For sorting
# Space Complexity - O(n)   => For Sort