# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # base case
        if (not head) or (not head.next):
            return head

        # assume our recursion is working fine and we have got the rest of the linked list reversed correctly!
        p = self.reverseList(head.next)

        # now all linked list except first is reversed and recived in p!! Yay!!
        # and - NOTE THIS -  our head - which was pointing to second element. And now second element is the tail of the finely reversed ll.
        # Thus our head is pointing to tail of the reversed linked list.
        # Hence :
        # head.next is tail of the linked list
        # and thus now AI is to set (tail_of_reverse_ll).next = head
        # thus we have to do (head.next).next = head
        head.next.next = head
        # now next of head should be None so -
        head.next = None
        return p
