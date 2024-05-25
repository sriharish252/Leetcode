from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initializing a dummy variable to sit at the beginning of the new merged LinkedList
        #   Helps with returning the head
        dummy = ListNode(0, None)
        temp = dummy
        # While there are two lists, merge them based on which is smaller
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # If list1 or list2 only remains assign that remaining list to the end of current merged list
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return dummy.next

# Time Complexity - O(n)
# Space Complexity - O(1)