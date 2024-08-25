from collections import deque
from Pagina import Pagina
from Heap import Heap
from Registro import Registro
import numpy as np

class Ordenador:
    def __init__(self):
        self.paginas:deque[Pagina] = deque()     
        self.nRegistros: int = 0
        self.betas: list[float] = []
        self.alpha_r: float = -1.0
        self.paginaFinal: deque[Registro] = None

    def ordenar(self, method:str,
                 m:int, k:int, r:int, n:int,
                   registros:list[int],
                     experimental: bool = False, to_print: bool = True) -> None:
        
        self.restart()
        self.paginas = self.criarPaginas(k)

        limite_de_paginas: int = self.setLimiteDePaginas(k, method)
        
        if not experimental:
            self.gerarSequencias(registros, m, r, limite_de_paginas)
        else:
            self.paginas = self.gerarRSequenciasAleatorias(n, r, k, method)
        
        match method:
            case "B":
                self.balanceadaMultiCaminhos(m, to_print)
            case "P":
                self.polifasica(m, to_print)
            case "C":
                self.cascata(m, to_print)
            case _:
                self.balanceadaMultiCaminhos(m, to_print)



    def restart(self) -> None:
        self.paginas.clear()
        self.nRegistros = 0
        self.betas.clear()
        self.alpha_r = -1.0
        self.paginaFinal = None

    def criarPaginas(self, k:int) -> None:
        paginas = deque()
        for i in range(k):
            paginas.append(Pagina(i))

        return paginas
    
    def gerarRSequenciasAleatorias(self, n, r, k, metodo):
                
        limite_de_paginas: int = self.setLimiteDePaginas(k, metodo)
            
        paginas: deque[Pagina] = self.criarPaginas(k)
        
        sequencia = deque()
        arquivos_possiveis: list[int] = self.permutacao(n)
        
        page_counter: int = 0
        seq_counter: int = 0
        n_registros: int = 0


        if(r % limite_de_paginas == 0):
            sequencia.append(Registro(arquivos_possiveis[n_registros]))
            n_registros+=1
            paginas[page_counter].add(sequencia, page_counter)
            sequencia = deque()
            r-=1
            
        while(seq_counter<r):
            if(len(sequencia)==0):
                sequencia.append(Registro(arquivos_possiveis[n_registros]))
                n_registros+=1
                continue

            if(sequencia[-1].value < Registro(arquivos_possiveis[n_registros]).value):
                sequencia.append(Registro(arquivos_possiveis[n_registros]))
                n_registros+=1
            else:
                paginas[page_counter].add(sequencia, page_counter)
                page_counter+=1
                seq_counter+=1
                page_counter%=limite_de_paginas
                sequencia = deque()

                     
        self.nRegistros = n_registros
        
        return paginas


    def permutacao(self, n:int) -> list[int]:
        return list(np.random.permutation(n))

    def gerarSequencias(self, registros:list[int],
                         m:int, r:int,
                           limitePaginas:int) -> None:
        heap = Heap()
        sequence:deque[Registro] = deque()
        sequencias = []
        pageCounter: int = 0
        sequenceCounter: int = 0
        count: int = 0

        for elem in registros:
            new_registro = Registro(elem)

            if (len(heap) < m):
                heap.push(new_registro)
                count+=1
                continue

            if (len(heap) == m and elem < heap.first().value):
                new_registro.setFlag()

            if (heap.first().flag == 1):
                heap.unflagAll()

            if (len(heap) == m): 
                sequence.append(heap.pop())
                heap.push(new_registro)

            if (not heap.isEmpty() and heap.first().flag == 1):
                sequencias.append(sequence)
                self.nRegistros += len(sequence)
                sequenceCounter+=1

                if(sequenceCounter == r): 
                    break

                sequence = deque()
            
            count+=1

        while(not heap.isEmpty()):
            sequence.append(heap.pop())
        
        self.nRegistros += len(sequence)

        if(sequencias.count(sequence)==0):
            sequencias.append(sequence)
        
        nPaginas = 0
        for elem in sequencias:
            self.paginas[nPaginas].add(elem, nPaginas)
            nPaginas+=1
            if(nPaginas == limitePaginas):
                nPaginas=0

        if(len(sequencias) % limitePaginas == 0):
            sequence = self.paginas[limitePaginas-1].popSequence()
            self.paginas[0].add(sequence, 0)


    def balanceadaMultiCaminhos(self, m:int, to_print:bool=True) -> None:
        count: int = 0
        writes: float = 0.0
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]

            self.computarResultados(filled, count, m, to_print)

            # roda o loop até que os primeiro arquivo de filled esteja vazio (terminou a intercalação da fase)
            while not filled[0].isEmpty():
                for x in notFilled:
                    if (self.isOrdered() or filled[0].isEmpty()):
                        break
                    writes += self.intercalar(filled, x)
                    [x.active() for x in filled if x.isBlocked()]
            
            count+=1

        filled = [x for x in self.paginas if (not x.isEmpty())]
        self.computarResultados(filled, count, m, to_print)
        self.paginaFinal = filled
        self.alpha_r = self.alpha(writes)
        if to_print:
            print("Final", f"{self.alpha_r:.2f}")
            
    def setLimiteDePaginas(self, k:int, metodo:str) -> int:
        if (metodo == "B"): 
            return k//2
        return k-1
        
    def intercalar(self, filled:deque[Pagina], target:Pagina) -> float:
        nWrites = 0.0
        heap = Heap()
        for x in filled:
            if(not x.isEmpty()):  #se a pagina está vazia eu simplesmente skipo ela
                heap.push(x.pop())
        
        new_sequence = deque()  #new_sequence representa a nova sequência que será gerada
        
        #intercalação propriamente dita utilizando heap mim
        while(len(heap) > 0):
            item = heap.pop()
            if (not self.paginas[item.index].isBlocked()):
                heap.push(self.paginas[item.index].pop())
            new_sequence.append(item)
            nWrites += 1

        target.add(new_sequence, target.index)
        return nWrites

    def polifasica(self, m, to_print: bool = True) -> None:
        count = 0
        writes = 0.0
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]
            smallest_subsequence_page = self.getSmallestPage(filled)

            self.computarResultados(filled, count, m, to_print)

            writes += self.intercalarPolifasica(smallest_subsequence_page, filled, notFilled[0])
            [x.active() for x in filled if x.isBlocked()]
            
            count+=1

        
        filled = [x for x in self.paginas if (not x.isEmpty())]
        self.computarResultados(filled, count, m, to_print)
        self.paginaFinal = filled
        self.alpha_r = self.alpha(writes)
        if to_print:
            print("Final", f"{self.alpha_r:.2f}")

    def intercalarPolifasica(self, smallest_page:Pagina, filled:deque[Pagina], target:Pagina) -> float:
        nWrites = 0.0
        heap = Heap()

        while(not smallest_page.isEmpty()):
            for x in filled:
                heap.push(x.pop())
            
            new_sequence = deque()  #new_sequence representa a nova sequência que será gerada

            #intercalação propriamente dita utilizando heap mim
            while(len(heap) > 0):
                item = heap.pop()
                if (not self.paginas[item.index].isBlocked()):
                    heap.push(self.paginas[item.index].pop())
                new_sequence.append(item)
                nWrites += 1
            target.add(new_sequence, target.index)

            [x.active() for x in filled if x.isBlocked()]

        return nWrites

    def cascata(self, m, to_print:bool=True) -> None:
        count = 0
        writes = 0.0

        # até sobrar apenas um arquivo
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]
            target = notFilled[0]

            self.computarResultados(filled, count, m, to_print)

            maiorPagina: Pagina = max(self.paginas, key=lambda x: len(x))

            # até que a maior pagina seja esvaziada, tem que continuar intercalando
            while(not maiorPagina.isEmpty()):
                writes += self.intercalar(filled, target)
                [x.active() for x in filled if x.isBlocked()]

                # se esvaziar alguma página no caminho, muda o alvo
                notFilled = [x for x in self.paginas if (x.isEmpty())]
                if (len(notFilled) != 0):
                    target = notFilled[0]
                    
            count+=1

        filled = [x for x in self.paginas if (not x.isEmpty())]
        self.paginaFinal = filled
        self.computarResultados(filled, count, m, to_print)
        self.alpha_r = self.alpha(writes)
        if to_print:
            print("Final", f"{self.alpha_r:.2f}")

    def getSmallestPage(self, filled:deque[Pagina]):
        smallest = filled[0]
        for i in range(1, len(filled)):
            if(filled[i].getSequencesCount() < smallest.getSequencesCount()):
                smallest = filled[i]
        return smallest
            


    #verifica se a ordenação finalizou
    def isOrdered(self) -> bool:
        count = 0
        for pagina in self.paginas:
            if (not pagina.isEmpty()):
                if( pagina.getSequencesCount() == 1):
                    count+=1
                else:
                    return False
        
        if count == 1: 
            return True
        
        return False

    #So organiza o print e calcula os resultados

    def beta(self, filled:list[Pagina], m):
        sequencesCount = 0
        for x in filled:
            sequencesCount+= x.getSequencesCount()
        
        b = (1/(m*sequencesCount))*self.nRegistros
        return b
    
    def alpha(self, writes):
        return round(writes/self.nRegistros,4)
        
        
    def computarResultados(self, filled:list[Pagina], count:int, m:int, to_print:bool=True):
        if to_print:
            print("Fase", count, end=" ")
        b = self.beta(filled, m)
        self.betas += [round(b,4)]

        if to_print:
            print(f"{b:.2f}")
            for x in filled:
                print(x.index+1, ": ", sep="", end="")
                x.imprimir() 
                print()

    def isAnyPageEmpty(self, pages:list[Pagina]):
        for page in pages:
            if (page.isEmpty()): 
                return True
        
        return False
    
    def isAllPagesEmpty(self, pages: deque[Pagina]):
        for page in pages:
            if (not page.isEmpty()):
                return False
            
        return True




            

                


                
            

            
            

            

            

            


                
