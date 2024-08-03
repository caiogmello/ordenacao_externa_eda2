import queue
from pagina import pagina
from Heap import Heap
from Registro import Registro

class ordenador:
    def __init__(self):
        self.paginas:list[pagina] = []
   
    def ordenar(self, method:str, m:int, k:int, r:int, registros:list[int]):
        self.criarPaginas(k)

    
    def criarPaginas(self, k:int):
        for i in k:
            self.paginas.append(pagina())
    
    def gerarSequencais(self, m:int, registros:list[int]) -> list[list:Registro]:
        heap = Heap(m)
        sequences:list[list:Registro] = []
        sequence:list[Registro] = []
        for elem in registros:


            new_registro = Registro(elem)
            if (len(heap) < m):
                heap.push(new_registro)
                continue
            if (len(heap) == m and elem < heap.first().value):
                 new_registro.setFlag()
            if (heap.first().flag == 1):
                heap.unflagAll()

            if (len(heap) == m):
                sequence.append(heap.pop())
                heap.push(new_registro)

            if (not heap.isEmpty() and heap.first().flag == 1):
                sequences.append(sequence)
                sequence = []
        
        while(not heap.isEmpty()):
            sequence.append(heap.pop())
        
        sequences.append(sequence)
        return sequences

                
