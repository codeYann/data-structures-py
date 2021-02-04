from node import Node

class Stack:
    # Link e tamanho da pilha
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, element): # Complexidade: O(1)
        # Inserindo um novo nó na pilha!
        newNode = Node(element)

        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top =  newNode
        self.size += 1
    
    def pop(self): # Complexidade: O(1)
        # Remove o topo da pilha!
        if not(self.size == 0):
            pointer = self.top
            self.top = self.top.next
        
            print("Valor removido => {}".format(pointer.data))
            self.size = self.size - 1
            return pointer
        else:
            raise IndexError("The stack's empty!")

    def peek(self): # Complexidade: O(1)
        # Retorna o top sem modificar a pilha
        if not(self.size == 0):
            return self.top
        else:
            raise IndexError("The stack is empty!")


    def __len__(self):
        # Retorna o tamanho da pilha
        return self.size
    
    def display(self): # Complexidade: O(n)
        # Mostra todos os nós que a pilha possui
        pointer = self.top
        while pointer != None:
            print("|{}|".format(pointer.data))
            pointer = pointer.next
        
    def search(self, element): # Complexidade: O(n)
        # Busca linear na pilha
        pointer = self.top
        index = 0
        while pointer != None:
            if pointer.data == element:
                return index
            else:
                pointer = pointer.next
                index += 1
        
    
