from collections import deque
from Pagina import Pagina
from Heap import Heap
from Registro import Registro

class Ordenador:
    def __init__(self):
        self.paginas:deque[Pagina] = deque()     
        self.nRegistros = 0
        self.betas = []
        self.alpha = -1.0
        self.paginaFinal = None

    def ordenar(self, method:str,
                 m:int, k:int, r:int, n:int,
                   registros:list[int], teste: bool = False, to_print: bool = True) -> None:
        self.criarPaginas(k)
        if (method == "B"): 
            limitePaginas = k//2
        else: 
            limitePaginas = k-1
        
        if not teste:
            self.gerarSequencais(registros, m, r, limitePaginas)
        if teste:
            print(m, r, limitePaginas)
            self.paginas = self.gerarRSequencias(n, r, k, method)
        
        match method:
            case "B":
                self.balanceadaMultiCaminhos(m)
            case "P":
                self.polifasica(m)
            case "C":
                self.cascata(m)
            case _:
                self.balanceadaMultiCaminhos(m)

        self.paginas.clear()
        self.nRegistros = 0


    def criarPaginas(self, k:int) -> None:
        for i in range(k):
            self.paginas.append(Pagina(i))
    
    def gerarRSequencias(self, n, r, k, metodo):
        import random
                
        limite_de_paginas = k-1
        if metodo == "B":
            limite_de_paginas = k//2
            
        paginas = deque()
        for i in range(k):
            paginas.append(Pagina(i))
        
        usados = [0]*n

        page_counter = 0
        sequencia = deque()
        seq_counter = 0
        n_registros = 0
        while(seq_counter<r):
            valor = random.randint(1,n)
            if usados[valor-1] == 1:
                continue
            else:
                n_registros+=1
                if(len(sequencia)==0):
                    sequencia.append(Registro(valor))
                    usados[valor-1] = 1
                else:
                    if(sequencia[-1].value < Registro(valor).value):
                        sequencia.append(Registro(valor))
                        usados[valor-1] = 1
                    else:
                        paginas[page_counter].add(sequencia, page_counter)
                        page_counter+=1
                        seq_counter+=1
                        n_registros-=1
                        page_counter%=limite_de_paginas
                        sequencia = deque()
                     
        self.nRegistros = n_registros
        
        return paginas

    
    def gerarSequencais(self, registros:list[int],
                         m:int, r:int,
                           limitePaginas:int) -> None:
        heap = Heap()
        sequence:deque[Registro] = deque()
        pageCounter = 0
        sequenceCounter = 0

        count = 0
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
                self.paginas[pageCounter].add(sequence, pageCounter)
                self.nRegistros += len(sequence)
                sequenceCounter+=1

                if(sequenceCounter == r): 
                    return
                pageCounter+=1

                if (pageCounter == limitePaginas): 
                    pageCounter = 0

                sequence = deque()
            
            count+=1
        
        while(not heap.isEmpty()):
            sequence.append(heap.pop())
        
        self.nRegistros += len(sequence)
        self.paginas[pageCounter].add(sequence, pageCounter)

    def balanceadaMultiCaminhos(self, m:int) -> None:
        count = 0
        writes = 0.0
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]

            self.imprimir_resultados(filled, count, m)

            for x in notFilled:
                if (self.isOrdered()):
                    break
                writes += self.intercalar(filled, x)
                [x.active() for x in filled if x.isBlocked()]
            
            count+=1

        
        filled = [x for x in self.paginas if (not x.isEmpty())]
        self.imprimir_resultados(filled, count, m)
        self.paginaFinal = filled
        self.alpha = self.calcular_alpha(writes)
        print("Final", f"{self.alpha:.2f}")
            
        
    def intercalar(self, filled:deque[Pagina], target:Pagina) -> float:
        nWrites = 0.0
        heap = Heap()
        for x in filled:
            if(x.isEmpty()):  #se a pagina está vazia eu simplesmente skipo ela
                pass
            else: heap.push(x.pop())
        
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

    def polifasica(self, m) -> None:
        count = 0
        writes = 0.0
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]

            self.imprimir_resultados(filled, count, m)

            
            writes += self.intercalarPolifasica(filled, notFilled[0])
            [x.active() for x in filled if x.isBlocked()]
            
            count+=1

        
        filled = [x for x in self.paginas if (not x.isEmpty())]
        self.imprimir_resultados(filled, count, m)
        self.paginaFinal = filled
        self.alpha = self.calcular_alpha(writes)
        print("Final", f"{self.alpha:.2f}")

    def intercalarPolifasica(self, filled:deque[Pagina], target:Pagina) -> float:
        nWrites = 0.0
        heap = Heap()

        while(not self.isAnyPageEmpty(filled)):
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

    def cascata(self, m) -> None:
        count = 0
        writes = 0.0

        # até sobrar apenas um arquivo
        while(not self.isOrdered()):
            filled = [x for x in self.paginas if (not x.isEmpty())]
            notFilled = [x for x in self.paginas if (x.isEmpty())]
            target = notFilled[0]

            self.imprimir_resultados(filled, count, m)

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
        self.imprimir_resultados(filled, count, m)
        self.alpha = self.calcular_alpha(writes)
        print("Final", f"{self.alpha:.2f}")


    #verifica se a ordenação finalizou
    def isOrdered(self) -> bool:
        count = 0
        for pagina in self.paginas:
            if (not pagina.isEmpty()): 
                count+=1
        
        if count == 1: 
            return True
        
        return False

    #So organiza o print e calcula os resultados

    def calcular_beta(self, filled:list[Pagina], m):
        sequencesCount = 0
        for x in filled:
            sequencesCount+= x.getSequencesCount()
        
        b = (1/(m*sequencesCount))*self.nRegistros
        return b
    
    def calcular_alpha(self, writes):
        return writes/self.nRegistros
        
        
    def imprimir_resultados(self, filled:list[Pagina], count:int, m:int):
        print("Fase", count, end=" ")
        b = self.calcular_beta(filled, m)
        self.betas += [b]

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




            

                


                
            

            
            

            

            

            


                
