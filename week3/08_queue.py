class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

queue = Queue()
queue.enqueue(1)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.is_empty())
