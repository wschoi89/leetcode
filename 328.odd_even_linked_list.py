from utils import LinkedList, ListNode
from typing import Optional

L1 = LinkedList()
L1.inserts([1, 2, 3, 4, 5])

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:

    odd_cur = head
    if odd_cur is None: # []
        return odd_cur

    if odd_cur.next is None:  # [1]
        return odd_cur

    even_head = odd_cur.next
    even_cur = even_head

    while even_cur and even_cur.next:
        odd_cur.next = even_cur.next
        odd_cur = odd_cur.next

        even_cur.next = odd_cur.next
        even_cur = even_cur.next

    odd_cur.next = even_head

    return head





result = oddEvenList(L1.head)
result.print_all()
