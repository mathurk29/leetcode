# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self) -> None:
        pass


""" Commenting my code as it is wrong """

# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#     l3 = ListNode()

#     c1 = l1
#     c2 = l2
#     c3 = l3

#     len_c1 = 1
#     len_c2 = 1
#     while c1.next:
#         len_c1 += 1
#         c1 = c1.next
#     while c2.next:
#         len_c2 += 1
#         c2 = c2.next

#     diff, node = ((len_c1 - len_c2),
#                   c2) if len_c1 > len_c2 else ((len_c2 - len_c1), c1)

#     for _ in range(diff):
#         node.next = ListNode()

#     carry_fwd = 0

#     c1 = l1
#     c2 = l2
#     c3 = l3

#     while c1 and c2:

#         c3.val = c1.val + c2.val + carry_fwd
#         if c3.val >= 10:
#             temp = c3.val
#             c3.val = temp % 10
#             carry_fwd = temp // 10

#         c3.next = ListNode()
#         c3 = c3.next

#         c1 = c1.next
#         c2 = c2.next
#     if carry_fwd:
#         c3.next = ListNode(carry_fwd)
#     return l3


# https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)  # Important
            n = n.next
        return root.next  # Important trick for LL!


# Driver code
sol = Solution()

L1 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)

L2 = ListNode(
    9,
    ListNode(
        9,
        ListNode(
            9,
            ListNode(
                9,
            ),
        ),
    ),
)

sol.addTwoNumbers(l1=L1, l2=L2)
