from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initializing a dummy variable to sit at the beginning of the LinkedList
        # Using dummy variable helps with the cases where the head node must be deleted
        dummy = ListNode(0, head)
        nodeBeforeNthNode, lastNode = dummy, head

        # Moving the lastNode to be n+1 distance from nodeBeforeNthNode
        while n>0 and lastNode:
            lastNode = lastNode.next
            n -= 1
        
        # Moving the lastNode to the end of the list.
        #   When this iteration is done:
        #       lastNode will be None
        #       nodeBeforeNthNode will be one node before the node to be deleted
        while lastNode:
            lastNode = lastNode.next
            nodeBeforeNthNode = nodeBeforeNthNode.next
        
        # Deleting the nodeBeforeNthNode from the end
        nodeBeforeNthNode.next = nodeBeforeNthNode.next.next
        
        # Head will be the next node from Dummy, since we initially assigned dummy.next to head
        return dummy.next

# Time Complexity - O(n)
# Space Complexity - O(1)