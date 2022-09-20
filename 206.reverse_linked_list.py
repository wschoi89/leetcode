from coding_interview.utils import LinkedList, ListNode

linked_list = LinkedList()
linked_list.inserts([1, 2, 3, 4, 5])
# output : 5->4->3->2->1->NULL
linked_list.print()


def reverse_list(head: ListNode) -> ListNode:

    prev = None
    cur = head

    while cur:
        # post = cur.next
        # cur.next = prev
        # prev = cur
        # cur = post

        post, cur.next = cur.next, prev

        prev, cur = cur, post

    return prev


result = reverse_list(linked_list.head)
result.print_all()









    # cur, prev = head, None
    #
    # while cur:
    #     next, cur.next = cur.next, prev
    #     prev, cur = cur, next
    #
    # return prev
