class MyStack:

    def __init__(self):
        from collections import deque

        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        last = self.deque.pop()
        return last

    def top(self) -> int:
        return self.deque[-1]

    def empty(self) -> bool:
        return len(self.deque) == 0


# Your MyStack object will be instantiated and called as such:
my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.top())
print(my_stack.pop())
print(my_stack.empty())

