from utils import LinkedList, ListNode
from typing import Optional

l1 = LinkedList([1, 2, 3, 4, 5])
left, right = 2, 4


def reverseBetween(self, head: Optional[ListNode], left: int, right: int):
    # phase 1
    dummy = ListNode(0, head)

    left_prev, cur = dummy, head
    for _ in range(left - 1):
        left_prev = cur
        cur = cur.next
    
    # phase 2
    # now cur="left", leftPrev="node before left"
    # reverse from left to right
    prev = None
    for i in range(right - left + 1):
        tmpNext = cur.next
        cur.next = prev
        prev = cur
        cur = tmpNext

    # phase 3
    # update pointers
    left_prev.next.next = cur
    left_prev.next = prev

    return dummy.next