# Definition for singly-linked list.

from utils import LinkedList, ListNode
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        from collections import deque
        dq = deque()  # deque 설정
        print(dq)
        while head is not None:
            dq.append(head.val)  # dq에 값을 추가
            head = head.next  # 다음 리스트 주소가 저장된 next를 사용할 head로 지정.

        print(dq)

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True


l1 = LinkedList([1,1,2,1])
l1.print()
print(Solution().isPalindrome(l1.head))