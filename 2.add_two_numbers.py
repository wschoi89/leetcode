# add two numbers


# l1 = 2->4->3
# l2 = 5->6->4

# 342 + 465 = 807
# output = 7->0->8


from coding_interview.utils import LinkedList, ListNode


l1 = LinkedList()
l1.inserts([2, 4, 3])
l1.print()

l2 = LinkedList()
l2.inserts([5, 6, 4])
l2.print()


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        val_1 = l1.val if l1 else 0
        val_2 = l2.val if l2 else 0

        val = val_1 + val_2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


result = add_two_numbers(l1.head, l2.head)
result.print_all()
