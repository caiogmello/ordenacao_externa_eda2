from heapq import *

class Heap:
    def __init__(self, memory: int):
        self.heap = []
    
    def push(self, item):
        heappush(self.heap, item)
    
    def pop(self):
        return heappop(self.heap)
    
    def first(self):
        return self.heap[0]
    
    def __len__(self):
        return len(self.heap)
    
    def __getitem__(self, index):
        return self.heap[index]
    
    def __str__(self):
        return str(self.heap)  
