from fileManager import fileManager
from value import value
import queue

if __name__ == "__main__":
    q = queue.PriorityQueue()
    q.put(value(5,0))
    q.put(value(2,1))
    q.put(value(10,1))


    for i in range(3):
        print(q.get().value)
    