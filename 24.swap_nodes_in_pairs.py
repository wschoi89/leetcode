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

    if head is None or head.next is None:
        return head
    
    prev = ListNode()
    dummy = head.next
    cur = head

    while cur and cur.next:
        post = cur.next
        next_pair = post.next

        post.next = cur
        cur.next = next_pair

        prev.next = post
        prev = cur
        cur = next_pair

    return dummy



result = swapPairs(linked_list.head)
result.print_all()