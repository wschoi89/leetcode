# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        from collections import deque

        values = deque()
        cur = head

        while cur.next is not None:
            values.append(cur.val)
            cur = cur.next
        values.append(cur.val)

        if values == values[::-1]:
            return True
        else:
            return False
