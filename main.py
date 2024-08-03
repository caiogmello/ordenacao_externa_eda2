from fileManager import fileManager
from Registro import Registro
import queue
from heapq import *

if __name__ == "__main__":
    heap = []
    heappush(heap, Registro(5))
    heappush(heap, Registro(2,1))
    heappush(heap, Registro(10))

    while len (heap) > 0: 
        print(heap[0].value)
        heappop(heap)