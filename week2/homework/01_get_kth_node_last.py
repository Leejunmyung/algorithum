class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        one = self.head
        length = 1
        while one.next is not None:
            one = one.next
            length += 1

        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur

    def get_kth_node_from_last2(self, k):
        first = self.head
        end = self.head
        for i in range(k):
            end = end.next

        while end is not None:
            end = end.next
            first = first.next
        return first





linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last2(3).data)  # 7이 나와야 합니다!