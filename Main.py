from helper.FileManager import fileManager
from structures.Ordenador import Ordenador
import sys
from helper.GeradorExperimentos import GeradorExperimentos


''''
    Note:

    Main.py
    Main file to run the project
    Usage:
        python3 Main.py [file]
    Example:
        python3 Main.py examples/hard_example

    to Output the results to a file, use the following command:
        python3 Main.py examples/hard_example > output.txt

'''

if __name__ == "__main__":
    g = GeradorExperimentos(3, 8, 200000)

    if(len(sys.argv) > 1):
        mode, specs, values = fileManager.read(f'{sys.argv[1]}')
    else:
        mode, specs, values = fileManager.read('examples/cascata')

    ordenador = Ordenador()
    
    # m,k,r,n
    ordenador.ordenar(mode, specs[0], specs[1], specs[2], specs[3], values)
