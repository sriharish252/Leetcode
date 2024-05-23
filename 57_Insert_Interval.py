from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(intervals)):
        # If newInterval can be inserted before the current interval
        #   We can say that the following intervals won't be overlapping in this case
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return (res + intervals[i:])
        # If newInterval goes after the current interval, append only the current interval to the result
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # If newInterval is overlapping, the min of the first index and the max of the second index
        #   of the current interval and newInterval, will be the new interval
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    # If 2nd IF or else case occurs, we need to append the newInterval to the result
    res.append(newInterval)
    return res

# Time Complexity - O(n)
# Space Complexity - O(n)