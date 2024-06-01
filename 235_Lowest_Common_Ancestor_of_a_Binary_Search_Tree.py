from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If currentNode is less than the search target (p and q)
        #   then we need to search the right subtree
        if (root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # If currentNode is greater than the search target (p and q), search left subtree
        elif (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        # If currentNode is between both p and q, then this is the common ancestor
        else:
            return root

# Time Complexity - O(n)
# Space Complexity - O(1)