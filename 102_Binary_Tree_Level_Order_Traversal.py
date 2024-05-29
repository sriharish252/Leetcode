from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    queue = [root]
    res = []
    while queue:
        currentLevel = []
        for i in range(len(queue)):
            temp = queue.pop(0)
            if temp:
                currentLevel.append(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
        if currentLevel:
            res.append(currentLevel)
    return res

# Time Complexity - O(n)
# Space Complexity - O(n) => Actually O(n/2) since the maximum data stored in the queue at a time will be n/2