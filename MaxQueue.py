from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()
        self.max_value = None

    def add(self, x: object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add
        """
        if self.max_value is None or x > self.max_value:
            self.max_value = x
        while self.max_deque.size() > 0 and x > self.max_deque.get(self.max_deque.size() - 1):
            self.max_deque.remove(self.max_deque.size() - 1)
        self.max_deque.add(self.max_deque.size(), x)
        super().add(x)

    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        x = super().remove()
        if x == self.max_value:
            self.max_deque.remove(0)
            if self.max_deque.size() > 0:
                self.max_value = self.max_deque.get(0)
            else:
                self.max_value = None
        return x

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)
    