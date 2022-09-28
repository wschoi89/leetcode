from coding_interview.utils import LinkedList, ListNode
from typing import Optional

L1 = LinkedList()
L1.inserts([1, 2, 3, 4, 5, 6, 7, 8])

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:

    head_odd = head
    head_even = head_odd.next

    cur_odd = head_odd
    cur_even = head_even

    while cur_even and cur_even.next:
        post_odd = cur_odd.next.next if cur_odd.next else None
        post_even = cur_even.next.next if cur_even.next else None

        cur_odd.next = post_odd
        cur_even.next = post_even

        cur_odd = post_odd
        cur_even = post_even

    cur_odd.next = head_even

    return head_odd


result = oddEvenList(L1.head)
result.print_all()


