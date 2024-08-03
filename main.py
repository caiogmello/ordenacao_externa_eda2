from fileManager import fileManager
from Registro import Registro
from ordenador import ordenador

if __name__ == "__main__":
    ordenador = ordenador()
    
    mode, specs, values = fileManager.read('example1')

    print(ordenador.gerarSequencais(specs[0], values))
