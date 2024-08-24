import matplotlib.pyplot as plt
from FileManager import fileManager
from Registro import Registro
from Ordenador import Ordenador
import sys
from tqdm import tqdm
import json

class GeradorExperimentos:
    def __init__(self, m:int=3, k:int=8, r:int=20):
        self.possibles_r = None
        self.initR()
        self.m = [3,15,30,45,60]
        self.k = [4,6,8,10,12]

        self.const_k = k
        self.const_m = m
        self.const_r = r

        self.ordenador = Ordenador()
    
    def initR(self):
        possibles = [i*j for i in range(1,11) for j in range(10,1001,10) if i*j <= 5000]
        sett = set(possibles)
        self.possibles_r = sorted(list(sett))

    
    def getAlphaDict(self, n:int, mode:str, numero_de_iteracoes:int=10):
        dct = {}
        with tqdm(total=len(self.possibles_r)) as pbar:
            for i in self.possibles_r:
                pbar.set_postfix_str(f"R: {i}")
                pbar.update(1)  
                for j in self.k:
                    alpha_total = 0
                    if i not in dct:  
                        dct[i] = {}
                    if j not in dct[i]:
                        dct[i][j] = {}
                    for l in range(numero_de_iteracoes):
                        self.ordenador.ordenar(mode, self.const_m, j, i, n, None, True, False)
                        alpha_total += self.ordenador.alpha

                    dct[i][j] = round(alpha_total/numero_de_iteracoes,4)

        return dct 
    

    def getBetaDict(self, n:int, mode:str, numero_de_iteracoes:int=10):
        dct = {}
        for j in self.m:
            beta0_total = 0
            if j not in dct:
                dct[j] = {}
            for l in range(numero_de_iteracoes):
                self.ordenador.ordenar(mode, j, self.const_k,self.const_r, n, None, True, False)
                beta0_total += self.ordenador.betas[0]

            dct[j] = round(beta0_total/numero_de_iteracoes,4)

        return dct
    
    def saveToJson(self, dct:dict, title:str):
        json.dump(dct, open(title, "w"))

    


    

    



