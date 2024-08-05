from FileManager import fileManager
from Registro import Registro
from Ordenador import ordenador

if __name__ == "__main__":
    
    # exemplo balanceada
    # mode, specs, values = fileManager.read('example1')

    # exemplo polifasica
    mode, specs, values = fileManager.read('hard_example')

    # exemplo cascata
    # mode, specs, values = fileManager.read('hard_example2')

    ordenador = ordenador()
    ordenador.ordenar(mode, specs[0], specs[1], specs[2], specs[3], values)
