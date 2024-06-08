from typing import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # Given array is not sorted, so we sort
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        # If beginning of interval is greater than current result ending,
        #       then no need to merge, just append
        if intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        # Else merge. We update only the ending value 
        #       since the lowest beginning value is already present due to the sort.
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
    return result

# Time Complexity - O(n*logn)
# Space Complexity - O(1)