class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        new_node = Node(data=data)
        new_node.setNext(new_next=self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, node_data):
        current = self.head
        is_present = False
        while current and not is_present:
            if current.getData() == node_data:
                is_present = True
            else:
                current = current.getNext()
                if not current:
                    raise ValueError('Data not present.')
        return current

    def delete(self):
        current = self.head
        previous = None
        is_present = False
        while current and not is_present:
            if current.getData() == node_data:
                is_present = True
            else:
                previous = current
                current = current.getNext()
                if not current:
                    raise ValueError('Data is not present.')
                if not previous:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next