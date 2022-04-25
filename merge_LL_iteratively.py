# https://leetcode.com/problems/merge-two-sorted-lists/submissions/  time 15:10

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # keep track of head of new list and tail to add on to
        head = ListNode()
        tail = head

        # iterate until we reach end of either list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # IMPORTANT: couldn't figure out this
            # added to tail in above if-else.
            # so now nove tail.
            # you got confused with the current tail.next value -
            # so to imagine start with tail as head.
            # now in if-else we added a node on tail by setting it to tail.next
            # so now tail has to be moved to that node [it is irrelevant what that tail node has in next cz we will compare two heads in next iteration and set it to that]
            # thus tail = tail.next

            tail = tail.next

        tail.next = list1 if list1 is not None else list2

        return head.next
