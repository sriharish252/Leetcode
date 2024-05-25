from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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