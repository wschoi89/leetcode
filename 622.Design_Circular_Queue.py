class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * (k)
        self.f = 0 # front
        self.r = 0 # rear
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.r] is None:
            self.queue[self.r] = value
            self.r = (self.r + 1) % len(self.queue)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue[self.f] is None:
            return False
        else:
            self.queue[self.f] = None
            self.f = (self.f + 1) % len(self.queue)

    def Front(self) -> int:
        return self.queue[self.f] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.r-1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.f == self.r

    def isFull(self) -> bool:
        r = 0 if self.r == len(self.queue) - 1 else self.r + 1

        return r == self.f



cq = MyCircularQueue(3)
print(cq.enQueue(1))
print(cq.Rear())
print(cq.enQueue(2))
print(cq.Rear())
print(cq.enQueue(3))
print(cq.Rear())
print(cq.enQueue(4))
print(cq.Rear())

print(cq.Rear())
print(cq.isFull())
print(cq.deQueue())
print(cq.enQueue(4))
print(cq.Rear())


