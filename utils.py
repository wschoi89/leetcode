import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_from_current(self):
        cur = self

        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print("")


class LinkedList:
    def __init__(self, values: iter):
        self.head = None
        self.tail = None

        if values:
            self.inserts(values)

    def insert(self, value):
        node = ListNode(value)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def inserts(self, values:iter):
        for value in values:
            self.insert(value)

    def print(self):
        cur = self.head
        print('linked list:', end=" ")
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()


def my_timer(func):
    def wrapper(s):
        t_start = time.perf_counter()
        print(func(s))
        print(f" {func.__name__} 실행 시간: {time.perf_counter() - t_start}")
    return wrapper



def print_linked_list(head_node: ListNode):
    cur = head_node
    while cur:
        print(cur.val, end=" ")
        cur = cur.next



