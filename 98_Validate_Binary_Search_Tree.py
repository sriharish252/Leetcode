from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root: Optional[TreeNode], min: int, max: int):
            if root:
                if root.val<=min or root.val>=max:
                    return False
                return isBST(root.left, min, root.val) and isBST(root.right, root.val, max)
            return True
        return isBST(root, -float("inf"), float("inf"))

# Time - O(n)
# Space - O(1)