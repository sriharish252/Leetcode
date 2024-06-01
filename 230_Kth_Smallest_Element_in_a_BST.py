from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, result = 0, -1
        def inorderTraversal(root: Optional[TreeNode]):
            nonlocal count, result
            if root is None:
                return
            inorderTraversal(root.left)
            count += 1
            if count==k:
                result = root.val
                return
            inorderTraversal(root.right)
        
        inorderTraversal(root)
        return result

# Time Complexity - O(n)
# Space Complexity - O(1)