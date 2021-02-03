# Class Node
class Node:
    def __init__(self, data):
        # criando um inteiro qualquer e chamado de data
        self.data = data
        # Mecanismo de link para unir os nós das listas!
        self.next = None
        self.prev = None
