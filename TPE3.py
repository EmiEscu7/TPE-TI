import math
import numpy as np

class TPE3():

    def calcularPasajeMoneda(self, moneda):
        retorno = []
        i = 0
        retorno.append(1) #primer valor se amntiene
        while (i < (len(moneda)-1)):
            s1 = int(moneda[i])
            s2 = int(moneda[i+1])
            if (s1<s2):
                retorno.append(0)
            elif (s1==s2):
                retorno.append(1)
            elif (s1>s2):
                retorno.append(2)
            i = i + 1
        return retorno

    def get_probabilities(self, matriz):
        prob = [0, 0, 0] #pos 0 sube. pos 1 mantiene. pos 2 baja
        i = 0
        for fila in matriz:
            for val in fila:
                prob[i] = prob[i] + val
            prob[i] = (prob[i]/3)
            i = i + 1
        return prob

    def calcularCanal(self, moneda, lista1, lista2, probs):
        retorno = [ [0,0,0], # Primer Columna sube, segunda columna mantiene, tercer columna baja
                    [0,0,0], # Primer fila sube, segunda fila mantiene, tercer fila baja
                    [0,0,0] ]
        i = 0
        while (i < len(lista1)):
            if (lista1[i] == 0):
                if (lista2[i] == 0):
                    retorno[0][0] = retorno[0][0] + 1
                elif (lista2[i] == 1):
                    retorno[1][0] = retorno[1][0] + 1
                elif (lista2[i] == 2):
                    retorno[2][0] = retorno[2][0] + 1
            elif (lista1[i] == 1):
                if (lista2[i] == 0):
                    retorno[0][1] = retorno[0][1] + 1
                elif (lista2[i] == 1):
                    retorno[1][1] = retorno[1][1] + 1
                elif (lista2[i] == 2):
                    retorno[2][1] = retorno[2][1] + 1
            elif (lista1[i] == 2):
                if (lista2[i] == 0):
                    retorno[0][2] = retorno[0][2] + 1
                elif (lista2[i] == 1):
                    retorno[1][2] = retorno[1][2] + 1
                elif (lista2[i] == 2):
                    retorno[2][2] = retorno[2][2] + 1
            i = i + 1
        columna = [0,0,0] 
        columna[0] += retorno[0][0] + retorno[1][0] + retorno[2][0] #cantidad que suben
        columna[1] += retorno[0][1] + retorno[1][1] + retorno[2][1] #cantidad que mantienen
        columna[2] += retorno[0][2] + retorno[1][2] + retorno[2][2] #cantidad que bajan
        j = 0
        while (j <= 2):
            k = 0
            while (k <= 2):
                retorno[j][k] = ((retorno [j][k]/columna[k]))
                k = k + 1
            j = j + 1
        return retorno
    

    def get_ruidito(self, canal):
        ruidito = np.zeros(len(canal[0]))
        i = 0
        for fila in canal:
            for valor in fila:
                if(valor != 0):
                    ruidito[i] += (valor * math.log2(valor))
                i += 1
            i = 0
        return ruidito  


    def get_perdidita(self, canal):
        perdidita = np.zeros(len(canal[0]))
        i = 0
        for fila in canal:
            suma = 0
            for valor in fila:
                suma += (valor * math.log2(valor))
            perdidita[i] = suma
            i += 1
        return perdidita

    def get_perdida_canal(self, prob, canal):
        perdidita = self.get_perdidita(canal)
        print(perdidita)
        perdida = 0
        i = 0
        while(i < len(perdidita)):
            perdida += prob[i]*(-perdidita[i])    
            i += 1
        return perdida

    def get_ruido_canal(self, prob, canal):
        ruidito = self.get_ruidito(canal)
        #print(ruidito)
        ruido = 0
        i = 0
        while(i < len(ruidito)):
            ruido += prob[i]*(-ruidito[i])    
            i += 1
        #ruido_perdida = prob * (-ruidito_perdidita)
        return ruido
