from utils import LinkedList, ListNode

linked_list = LinkedList([1, 2, 3, 4, 5])

# output : 5->4->3->2->1->NULL
linked_list.print()


def reverse_list(head: ListNode) -> ListNode:

    prev = None

    while head:
        post = head.next

        head.next = prev

        prev = head
        head = post

    return prev


result = reverse_list(linked_list.head)

result.print_from_current()

