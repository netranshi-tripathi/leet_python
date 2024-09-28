class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k):
        self.size = 0
        self.capacity = k
        self.head = None
        self.rear = None

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            newHead = Node(value, self.head, None)
            self.head.prev = newHead
            self.head = newHead

        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            self.rear.next = Node(value, None, self.rear)
            self.rear = self.rear.next

        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.head = self.head.next

        self.size -= 1
        return True

    def deleteLast(self) :
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.rear = self.rear.prev

        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.head.val

    def getRear(self):
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity