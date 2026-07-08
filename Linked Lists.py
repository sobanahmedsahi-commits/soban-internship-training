class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def count_nodes(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

list= LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
print(list.count_nodes())
