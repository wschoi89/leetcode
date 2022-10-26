from utils import LinkedList, ListNode
from typing import Optional

list1 = LinkedList([1, 2, 4])

# list1.print()
list2 = LinkedList([1, 3, 4])

# list2.print()


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode()
    tail = dummy_node
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            tail = list1
            list1 = list1.next

        else:
            tail.next = list2
            tail = list2
            list2 = list2.next

    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummy_node.next


result = merge_two_lists(list1.head, list2.head)

print(result.print_from_current())








