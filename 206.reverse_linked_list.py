from coding_interview.utils import LinkedList, ListNode

linked_list = LinkedList()
linked_list.inserts([1, 2, 3, 4, 5])
# output : 5->4->3->2->1->NULL
linked_list.print()

head = linked_list.head

cur = None

while head is not None:
    new_node = ListNode(head.val)

    if cur is not None:
        new_node.next = cur

    cur = new_node

    head = head.next

print('cur: ', cur.print_all())
