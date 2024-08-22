from FileManager import fileManager
from Registro import Registro
from Ordenador import Ordenador
import sys


if __name__ == "__main__":
    
    # exemplo balanceada
    # mode, specs, values = fileManager.read('example1')

    # exemplo polifasica
    if(len(sys.argv) > 1):
        mode, specs, values = fileManager.read(sys.argv[1])
    else:
        mode, specs, values = fileManager.read('hard_example')

    # exemplo cascata
    # mode, specs, values = fileManager.read('hard_example2')

    ordenador = Ordenador()
    # m,k,r,n
    ordenador.ordenar(mode, specs[0], specs[1], specs[2], specs[3], values)
