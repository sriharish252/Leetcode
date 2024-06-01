from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap to store the count of each character
        countDict = {}
        # freqList stores count as index, number as value
        #   Used to retrieve the top k counts
        freqList = [[] for _ in range(len(nums)+1)]
        for n in nums:
            countDict[n] = 1+ countDict.get(n, 0)
        for num, count in countDict.items():
            freqList[count].append(num)
        
        result = []
        for i in range(len(freqList)-1, 0, -1):
            # If the list at that count has any value, 
            #   append them to the result
            for n in freqList[i]:
                result.append(n)
                if len(result) == k:
                    return result

# Time Complexity - O(n) => n: length of nums
# Space Complexity - O(n)