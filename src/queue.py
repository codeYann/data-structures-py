from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, element):
        node = Node(element)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
    
    def pop(self):
        if self.first is not None:
            pointer = self.first
            self.first = self.first.next
            self.size = self.size - 1
            return pointer
        else:
            raise IndexError("A fila está vazia")
    
    def __len__(self):
        return self.size
    
    def display(self):
        if self.first is not None:
            pointer = self.first
            while pointer != None:
                print("{}".format(pointer.data))
                pointer = pointer.next
        else:
            raise IndexError("A fila está vazia")

    def peek(self):
        return self.first