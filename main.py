from fileManager import fileManager
from Registro import Registro
from ordenador import ordenador

if __name__ == "__main__":
    
    # exemplo balanceada
    # mode, specs, values = fileManager.read('example1')

    # exemplo polifasica
    mode, specs, values = fileManager.read('example1-poli')

    # exemplo cascata
    # mode, specs, values = fileManager.read('example1-casca')

    ordenador = ordenador()
    ordenador.ordenar(mode, specs[0], specs[1], specs[2], specs[3], values)
