from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    sortedKeyDict = {}
    for s in strs:
        sortedS = ''.join(sorted(s))
        if sortedS not in sortedKeyDict:
            sortedKeyDict[sortedS] = []
        sortedKeyDict[sortedS].append(s)
    return sortedKeyDict.values()

# Time Complexity - O(k* n*log n) => k:number of strings, n:length of longest string
# Space Complexity - O(k*n)

# Can be optimized for time to O(k*n) by using characterCount as key instead of sorting