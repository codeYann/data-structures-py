from node import Node

class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, element, index):  # Complexidade: O(n)
        # Insere um novo elemento na lista
        newNode = Node(element)

        if index <= self.size:
            if self.head == None and self.tail == None:  # Complexidade: O(1)
                self.head = newNode
                self.tail = newNode

            elif index == 0:  # Complexidade: O(1)
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif index == self.size:  # Complexidade: O(1)
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

            else:  # Complexidade: O(n)
                pointer = self.head
                for _ in range(index):
                    pointer = pointer.next
                newNode.next = pointer
                newNode.prev = pointer.prev
                pointer.prev.next = newNode
                pointer.prev = newNode
            
            self.size += 1
        else:
            raise IndexError("List index out of range")

    def __len__(self):
        # Retorna o tamanho da lista
        return self.size

    def display(self): # Complexidade: O(n)
        # Percorre a lista e mostra o valor de cada nó
        pointer = self.head

        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def search(self, element): # Complexidade: O(n)
        # Busca por um elemento na lista e retorna sua posição
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
    
    def pop(self, index): # Complexidade: O(n)
        # Remove um nó da lista
        if index < self.size:
            if self.head.next == None:
                print("Valor removido => {}".format(self.head.data))
                self.head = None
                self.tail = None

            elif index == 0:
                print("Valor removido => {}".format(self.head.data))
                pointer = self.head
                self.head = self.head.next
                self.head.prev = None

            elif index == self.size - 1:
                pointer = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                print("Valor removido => {}".format(pointer.data))
            
            else:
                pointer = self.head
                for _ in range(index):
                    pointer = pointer.next
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                print("Valor removido => {}".format(pointer.data))

            self.size = self.size - 1
            return pointer
        else:
            raise IndexError("List index out of range")
