from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Idea: Merge every next two lists in the list at a time
        #           and then repeat the same with every 2 merged lists
        #       This way the elements in each merge is reduced and hence
        #           a part of time complexity becomes (log k) instead of k,
        #           where k is the number of lists
        if not lists or len(lists)==0:
            return None
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # Check if another list exists at index (i+1)
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            
            # Update lists with the mergedLists to continue to merge them until only 1 list remains
            lists = mergedLists
        
        # Return the beginning node of lists since it's the head
        return lists[0]
    
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

# Time Complexity - O(n * log k) => k: number of lists, n: largest number of elements in a list
# Space Complexity - O(n*k)