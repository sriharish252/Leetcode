from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Fast pointer moves two steps at a time and slow pointer moves 1 step at a time
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # If both are the same node then there is a cycle
        if slow == fast:
            return True
    return False

# Time Complexity - O(n)
# Space Complexity - O(1)