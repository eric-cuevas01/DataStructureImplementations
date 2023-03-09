from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n:
            raise IndexError()
        if i < self.n // 2:
            u = self.dummy.next
            for j in range(i):
                u = u.next
        else:
            u = self.dummy
            for j in range(self.n, i, -1):
                u = u.prev
        return u

    def get(self, i) -> object:
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError()
        self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        if self.n <= 1:
            return True
        left_node = self.dummy.next
        right_node = self.dummy.prev
        for i in range(self.n // 2):
            if left_node.x != right_node.x:
                return False
            left_node = left_node.next
            right_node = right_node.prev
        return True

    def reverse(self):
        """
        Reverses the doubly linked list in O(n) time.
        """
        node = self.dummy.next
        while node is not self.dummy:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev
        temp = self.dummy.prev
        self.dummy.prev = self.dummy.next
        self.dummy.next = temp

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
