

def sumTwinElements(head):

    # debug = head
    # while(debug):
    #     print(debug.val)
    #     debug = debug.next

    # print('Done')

    middle, fast = head, head

    # make slow point to middle of LL
    while fast and fast.next:
        fast = fast.next.next
        middle = middle.next

    # reverse LL from slow onwards hence set curr to middle

    curr, prev = middle, None

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # debug = prev
    # while(debug):
    #     print(debug.val)
    #     debug = debug.next

    # prev is the head of the second part of LL - so head and prev are the twins elements now

    # add head and prev and find the max

    result = 0
    while prev:
        result = max(result, head.val + prev.val)
        head = head.next
        prev = prev.next

    return result


class Node:
    def __init__(self, val, next=False) -> None:
        self.val = val
        self.next = next


Head = Node(1)

second_val = Node(2)
Head.next = second_val

third_val = Node(3)
second_val.next = third_val

fourth_val = Node(2)
third_val.next = fourth_val


sumTwinElements(Head)
