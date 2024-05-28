from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1+max(self.maxDepth(root.left),  self.maxDepth(root.right))

# Time Complexity - O(n)
# Space Complexity - O(1)