# https://leetcode.com/problems/merge-two-sorted-lists/solution/


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Step2: this is executed in the last of recursion

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Step 1:
        head = ListNode()

        if list1.val < list2.val:
            head = list1
            list1 = list1.next

        else:
            head = list2
            list2 = list2.next

        head.next = self.mergeTwoLists(list1, list2)

        return head


# Time complexity = O(m+n)
# Space complexity = O(m+n)
