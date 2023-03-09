import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n == 0:
            raise IndexError("Queue is empty")

            # Generate a random index within the range of valid indices for the current queue
        rand_idx = random.randrange(self.n)

        # Remove the element at the random index
        x = self.a[(self.j + rand_idx) % len(self.a)]
        self.a[(self.j + rand_idx) % len(self.a)] = None

        # Shift the elements after the random index to fill the gap
        for i in range(rand_idx + 1, self.n):
            self.a[(self.j + i - 1) % len(self.a)] = self.a[(self.j + i) % len(self.a)]

        # Update size and resize if necessary
        self.n -= 1
        if self.n < len(self.a) // 4:
            self.resize()

        return x

    def add(self, x: object):
        '''
            add element x at the end of the queue
        '''
        super().add(x)
