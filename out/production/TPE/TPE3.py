import math
import numpy as np

class TPE3():

    def get_probabilities(self, matriz):
        prob = [0, 0, 0] #pos 0 sube. pos 1 mantiene. pos 2 baja
        i = 0
        for fila in matriz:
            for val in fila:
                prob[i] += val
            prob[i] /= 3
            i += 1
        return prob
    

    def get_ruidito_perdidita(self, canal):
        ruidito_perdidita = np.zeros(len(canal[0]))
        i = 0
        for fila in canal:
            for valor in fila:
                if(valor != 0):
                    ruidito_perdidita[i] += (valor * math.log2(valor))
                i += 1
            i = 0
        return ruidito_perdidita    

    def get_ruido_perdida_canal(self, prob, canal):
        ruidito_perdidita = self.get_ruidito_perdidita(canal)
        ruido_perdida = prob * (-ruidito_perdidita)
        return ruido_perdida
