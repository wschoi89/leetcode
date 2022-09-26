from coding_interview.utils import LinkedList, ListNode

# Example 1
# input: [1, 2, 3, 4]
# output: [2, 1, 4, 3]

# Example 2
# input: []
# output: []

# Example 3
# input: [1]
# output: [1]

linked_list = LinkedList()
linked_list.inserts([1, 2, 3, 4])


from coding_interview.utils import LinkedList, ListNode

# Example 1
# input: [1, 2, 3, 4]
# output: [2, 1, 4, 3]

# Example 2
# input: []
# output: []

# Example 3
# input: [1]
# output: [1]

linked_list = LinkedList()
linked_list.inserts([1, 2, 3, 4])


def swapPairs(head: ListNode) -> [ListNode]:

    dummy = ListNode(0, head)

    prev, cur = dummy, head

    while cur and cur.next:
        # save ptrs
        next_pair = cur.next.next # 3
        second = cur.next # 2

        # reverse this pair
        second.next = cur # 2->1
        cur.next = next_pair # 2->1->3

        prev.next = second

        prev = cur
        cur = next_pair

    return dummy.next



result = swapPairs(linked_list.head)
result.print_all()

