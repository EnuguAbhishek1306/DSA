class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        value = [str(x) for x in self.linkedList]
        return " ".join(value)

    def enqueue(self, value):
        new = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new
            self.linkedList.tail = new
        else:
            self.linkedList.tail.next = new
            self.linkedList.tail = new

    def dequeue(self):
        if self.linkedList.head is None:
            return None
        else:
            poppedNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            poppedNode.next = None
            return poppedNode.value

    def peek(self):
        if self.linkedList.head is None:
            return None
        else:
            return self.linkedList.head.value

    def isempty(self):
        
            
        return  self.linkedList.head == None

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()

