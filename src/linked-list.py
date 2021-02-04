# Linked List implementation
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, element, index):  # Complexidade worst case: O(n)
        # Adiciona um nó na lista
        newNode = Node(element)

        if index <= self.size:
            if self.head == None:  # Complexidade: O(1)
                self.head = newNode
                self.tail = newNode

            elif index == 0:  # Complexidade: O(1)
                newNode.next = self.head
                self.head = newNode

            elif index == self.size:  # Complexidade: O(1)
                self.tail.next = newNode
                self.tail = self.tail.next

            else:  # Complexidade: O(n)
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next

                newNode.next = pointer.next
                pointer.next = newNode

            self.size += 1
        else:
            raise IndexError("List index out of range")

    def index(self, element):  # Complexidade: O(n)
        # Retorna a posição de acordo com o valor passado!
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
        # Retorna o tamanho da lista
        return self.size

    def display(self):  # Complexidade: O(n)
        # Percorre a lista e mostra todos os valores de cada nó
        pointer = self.head

        while pointer != None:
            print(pointer.data)
            pointer = pointer.next

    def pop(self, index): # Complexidade: O(n)
        # Remove um nó da lista
        if index < self.size:
            if index == 0:
                garbage = self.head
                self.head = self.head.next
                print("Valor removido {}".format(garbage.data))

            elif index == self.size:
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next
                garbage = pointer.next
                self.tail = pointer
                print("Valor removido {}".format(garbage.data))

            else:
                pointer = self.head
                for _ in range(index - 1):
                    pointer = pointer.next
                garbage = pointer.next
                pointer.next = pointer.next.next
                print("Valor removido {}".format(garbage.data))

            self.size = self.size - 1
            return garbage

        else:
            raise IndexError("List index out of range")