class MyQueue:

    def __init__(self):
        from collections import deque

        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.appendleft(x)

    def pop(self) -> int:
        return self.deque.pop()

    def peek(self) -> int:
        return self.deque[-1]

    def empty(self) -> bool:
        return len(self.deque) == 0