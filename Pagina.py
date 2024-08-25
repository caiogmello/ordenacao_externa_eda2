from collections import deque
from Registro import Registro

class Pagina:
    def __init__(self, index):
        self.registros:deque[deque] = deque()
        self.blocked = False
        self.index = index

    def getPageIndex(self) -> int:
        return self.index
    
    def get_smallest_subsequence(self):
        filled = [x for x in self.registros if(len(x) > 0)]
        if(len(filled) > 1):
            smallest = filled[0]
            for i in range(1, len(filled)):
                if (len(filled[i]) < len(smallest)):
                    smallest = filled[i]

            return smallest

    def get(self, index:int) -> int:
        if (self.registros[index] is not None):
            return self.registros[index]
        return -1

    def pop(self):
        if(len(self.registros) < 1):
            print(self.registros)
        item = self.registros[0].popleft()
        if (len(self.registros[0]) < 1): self.blocked = True
        return item
    
    def popSequence(self):
        return self.registros.popleft()
    
    def active(self):
        
        self.registros.popleft()
        
        self.blocked = False
    
    def isBlocked(self):
        return self.blocked

    def set(self, index:int, value:int):
        if(len(self.registros) > index):
            self.registros[index] = value

    def add(self, sequence:deque[Registro], index:int):
        for elem in sequence:
            elem.setIndex(index)
            elem.delFlag()
        self.registros.append(sequence)
    
    def getSequencesCount(self):
        return len(self.registros)

    def __str__(self):
        return str(self.registros)
    
    def imprimir(self):
        for elem in self.registros:
            print("{",sep="", end="")
            for i in range(len(elem)):
                if(i != len(elem)-1): print(elem[i], end=" ")
                else: print(elem[i], end="")

            print("}",sep="", end="")
                
    
    def __repr__(self):
        return str(self.registros)
    
    def isEmpty(self):
        return len(self.registros) < 1
    
    def __len__(self):
        qtdRegistros = 0
        for sequence in self.registros:
            qtdRegistros += len(sequence)

        return qtdRegistros
        
