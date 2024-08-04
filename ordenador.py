from collections import deque
from pagina import pagina
from Heap import Heap
from Registro import Registro

class ordenador:
    def __init__(self):
        self.paginas:deque[pagina] = deque()

    def isOrdered(self):
        count = 0
        for pagina in self.paginas:
            if (not pagina.isEmpty()): count+=1
        
        if count == 1: return True
        return False

   
    def ordenar(self, method:str, m:int, k:int, r:int, n:int, registros:list[int]):
        self.criarPaginas(k)
        if (method == "B"): limitePaginas = k//2
        else: limitePaginas = k-1
        self.gerarSequencais(m, registros, limitePaginas)
        self.balanceada_multi_caminhos(n, m)

    def criarPaginas(self, k:int):
        for i in range(k):
            self.paginas.append(pagina(i))
    
    def gerarSequencais(self, m:int, registros:list[int], limitePaginas:int) -> list[list:Registro]:
        heap = Heap()
        sequence:deque[Registro] = deque()
        pageCounter = 0
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
                self.paginas[pageCounter].add(sequence, pageCounter)
                pageCounter+=1
                if (pageCounter == limitePaginas): pageCounter = 0
                sequence = deque()
        
        while(not heap.isEmpty()):
            sequence.append(heap.pop())
        
        self.paginas[pageCounter].add(sequence, pageCounter)

    def balanceada_multi_caminhos(self, n:int, m:int):
        count = 0
        while(not self.isOrdered()):
            print("Fase", count, end=" ")
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]
            sequencesCount = 0
            for x in filled:
                sequencesCount+= x.getSequencesCount()
            b = (1/(m*sequencesCount))*n

            print(round(b, 2))
            for x in filled:
                print(x.index, ": ", sep="", end="")
                x.imprimir()
                print()

            for x in notFilled:
                if (self.isOrdered()) : break;
                self.intercalar(filled, x)
                [x.active() for x in filled if x.isBlocked()]
            
            count+=1

        print("Fase", count, end=" ")
        
        filled = [x for x in self.paginas if (not x.isEmpty())]
        sequencesCount = 0
        for x in filled:
            sequencesCount+= x.getSequencesCount()
        b = (1/(m*sequencesCount))*n

        print(round(b, 2))
        for x in filled:
                print(x.index, ": ", sep="", end="")
                x.imprimir()
                print()
            
        
    def intercalar(self, filled:deque[pagina], target:pagina):
        heap = Heap()

        for x in filled:
            if(x.isEmpty()):
                pass
            else: heap.push(x.pop())
        sequence = deque()
        while(len(heap) > 0):
            item = heap.pop()
            if (not self.paginas[item.index].isBlocked()):
                heap.push(self.paginas[item.index].pop())
            sequence.append(item)
    
        target.add(sequence, target.index)




            

                


                
            

            
            

            

            

            


                
