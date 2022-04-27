from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while(current):

            # save the next node loc as we are going to replace it's entry from current.next the with the prev node
            nextNode = current.next

            # actual reverse of LL - thus now you can iterate forward in next steps
            current.next = previous

            # to iterate fwd we have to move fwd both previous and current

            # since current is the next node of previous we iterate by moving previous to current
            previous = current
            # since nextNode is the next node of current we iterate by moving current to nextNode
            current = nextNode

            # if it reaches the end it will become None and iteration stops

        return previous
