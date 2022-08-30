from coding_interview.utils import LinkedList, ListNode
from typing import Optional

list1 = LinkedList()
list1.inserts([1, 2, 4])
# list1.print()
list2 = LinkedList()
list2.inserts([1, 3, 4])
# list2.print()

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
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

    while list1:
        tail.next = list1

    while list2:
        tail.next = list2


    return dummy_node.next

merge_two_lists(list1.head, list2.head)








