from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Idea: Reverse the list 2nd half of the list and merge the normal and reversed lists
        #        Find the middle with a slow and fast pointer
        slow, fast = head, head
        
        # When fast pointer reaches the last node or moves 1 step further, the slow points to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the nodes after the middle
        right = self.reverseList(slow.next)
        
        # Making the middle as the last node in the original list
        slow.next = None
        left = head

        # Merge the normal and reversed lists
        while left and right:
            leftNextNode = left.next
            rightNextNode = right.next
            left.next = right
            right.next = leftNextNode
            left = leftNextNode
            right = rightNextNode
        return head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, nextNode = None, None
        temp = head
        while temp:
            nextNode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextNode
        return prevNode

# Time Complexity - O(n)
# Space Complexity - O(1)