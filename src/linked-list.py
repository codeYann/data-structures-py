# Linked List implementation

from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, element, index):  # Complexity worst case: O(n)
        newNode = Node(element)

        if index <= self.size:
            if self.head == None:  # Complexity: O(1)
                self.head = newNode
                self.tail = newNode

            elif index == 0:  # Complexity: O(1)
                newNode.next = self.head
                self.head = newNode

            elif index == self.size:  # Complexity: O(1)
                self.tail.next = newNode
                self.tail = self.tail.next

            else:  # Complexity: O(n)
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next

                newNode.next = pointer.next
                pointer.next = newNode

            self.size += 1
        else:
            raise IndexError("List index out of range")

    def index(self, element):  # Complexity worst case: O(n)
        pointer = self.head
        i = 0

        while pointer != None:
            if pointer.data == element:
                return i
            else:
                pointer = pointer.next
                i += 1

        raise ValueError("{} is not in list".format(element))

    def __len__(self):
        return self.size

    def display(self):  # Complexity worst case: O(n)
        pointer = self.head

        while pointer != None:
            print(pointer.data)
            pointer = pointer.next

    def pop(self, index):

        if index < self.size:
            if index == 0:
                garbage = self.head
                self.head = self.head.next
                print("Valor removido {}".format(garbage.data))
                del garbage

            elif index == self.size:
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next
                garbage = pointer.next
                self.tail = pointer
                print("Valor removido {}".format(garbage.data))
                del garbage

            else:
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next
                garbage = pointer.next
                pointer.next = pointer.next.next
                print("Valor removido {}".format(garbage.data))
                del garbage

            self.size = self.size - 1

        else:
            raise IndexError("List index out of range")


Lista = LinkedList()

Lista.append(10, 0)
Lista.append(15, 1)
Lista.append(9, 0)

Lista.display()
Lista.pop(1)
Lista.display()