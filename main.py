from fileManager import fileManager
from Registro import Registro
import queue
from heapq import *
from Heap import Heap

if __name__ == "__main__":
    heap = Heap(3)

    heap.push(Registro(1))
    heap.push(Registro(10))
    heap.push(Registro(4))

    heap.flagAll()

    print(heap.isFullFlagged())

    heap.unflagAll()

    print(heap.isFullFlagged())

