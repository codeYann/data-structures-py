from node import Node


class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, element, index):  # Complexity worst case: O(n)
        newNode = Node(element)

        if index <= self.size:
            if self.head == None and self.tail == None:  # Complexity: O(1)
                self.head = newNode
                self.tail = newNode

            elif index == 0:  # Complexity: O(1)
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif index == self.size:  # Complexity: O(1)
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

            else:  # Complexity: O(n)
                pointer = self.head
                for i in range(index):
                    pointer = pointer.next
                newNode.next = pointer
                newNode.prev = pointer.prev
                pointer.prev.next = newNode
                pointer.prev = newNode
            
            self.size += 1
        else:
            raise IndexError("List index out of range")

    def __len__(self):
        return self.size

    def display(self):
        pointer = self.head

        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def search(self, element):
        pointer = self.head
        index = 0

        while pointer != None:
            if pointer.data == element:
                print(index)
                return index
            else:
                pointer = pointer.next
                index += 1
        
        raise ValueError("{} is not in list".format(element))
    
    def pop(self, index):
        if index < self.size:
            if self.head.next == None:
                print("Valor removido => {}".format(self.head.data))
                self.head = None
                self.tail = None

            elif index == 0:
                print("Valor removido => {}".format(self.head.data))
                garbage = self.head
                self.head = self.head.next
                self.head.prev = None
                del garbage

            elif index == self.size - 1:
                garbage = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                print("Valor removido => {}".format(garbage.data))
                del garbage
            
            else:
                pointer = self.head
                for _ in range(index):
                    pointer = pointer.next
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                print("Valor removido => {}".format(pointer.data))
                del pointer

            self.size = self.size - 1
        else:
            raise IndexError("List index out of range")
Lista = DoublyList()

Lista.append(15, 0)
Lista.append(20, 1)
Lista.append(14, 0)
Lista.append(25, 1)

Lista.display()

Lista.pop(3)

Lista.display()