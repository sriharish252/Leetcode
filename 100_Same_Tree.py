from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are none, then they are same, so true
        if p is None and q is None:
            return True
        # If 1 is none and the other has value or if are not none and their values are different
        if p is None or q is None or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# Time Complexity - O(p+q)
# Space Complexity - O(1)