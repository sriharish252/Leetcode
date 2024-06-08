from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sum = 0
    dummyHead = ListNode(0, None)
    currentNode = dummyHead
    while l1 or l2 or sum:
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        currentNode.next = ListNode(sum%10)
        # Update the carryOver in the sum
        sum = sum//10
        currentNode = currentNode.next
    return dummyHead.next

# Time Complexity - O(n)
# Space Complexity - O(1)