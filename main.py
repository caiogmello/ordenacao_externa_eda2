from fileManager import fileManager
from Registro import Registro
import queue
from Heap import Heap

if __name__ == "__main__":
    heap = Heap(3)
    heap.push(Registro(5))
    new_registro = Registro(2)
    new_registro.setFlag()
    heap.push(new_registro)
    heap.push(Registro(10))

    while len (heap) > 0: 
        print(heap.first().value)
        heap.pop()