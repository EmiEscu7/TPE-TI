import random
import sys
import numpy as np
import linecache
import math
import matplotlib.pyplot as plt 


class TPE1:

    def calcular_matriz_pasaje(self, moneda):

        retorno = [ [0,0,0], # Primer Columna sube, segunda columna mantiene, tercer columna baja
                    [0,0,0], # Primer fila sube, segunda fila mantiene, tercer fila baja
                    [0,0,0] ]
        t_actual = 0
        total_retornos = [0,0,0]
        ult_retorno = 0
        ult_retorno_columna = 0
        s = 0

        while (t_actual < 1000):
            s = int(moneda[t_actual])
            t_actual = t_actual+1
            total_retornos[ult_retorno_columna] = total_retornos[ult_retorno_columna]+1
            if (s > ult_retorno):
                retorno[0][ult_retorno_columna] = retorno[0][ult_retorno_columna]+1
                ult_retorno_columna = 0
            elif (s == ult_retorno):
                retorno[1][ult_retorno_columna] = retorno[1][ult_retorno_columna]+1
                ult_retorno_columna = 1
            else: # Si fue menor
                retorno[2][ult_retorno_columna] = retorno[2][ult_retorno_columna]+1
                ult_retorno_columna = 2
            ult_retorno = s
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                retorno[i][j] = retorno[i][j]/total_retornos[j]
                j += 1
            i += 1
        return retorno

    def calcular_autocorrelacion(self, moneda, tau_min, tau_max):
        autocorrelacion = np.zeros(tau_max+1)
        tau = tau_min
        t_actual = 0
        tamanio = len(moneda)
        while(tau <= tau_max):
            while (tau + t_actual < tamanio):
                s1 = int(moneda[t_actual])
                s2 = int(moneda[t_actual+tau])
                t_actual += 1
                autocorrelacion[tau] += s1*s2
            autocorrelacion[tau] /= t_actual
            t_actual=0
            tau += 1
        return autocorrelacion[1:51]

    def calcular_media(self, moneda, tamanio):
        media = 0
        for valor in moneda:
            media += int(valor)     
        media /= tamanio
        return media

    def calcular_varianza(self, moneda, tamanio, media):
        varianza = 0
        for valor in moneda:
            varianza += pow(int(valor) - media,2)   
        varianza /= tamanio
        return varianza

    def calcular_correlacion(self, a, b, tau):
        acum = 0
        i = 0
        while (i <= (999 - tau)):
            d1 = int(a[i])
            d2 = int(b[(i + tau)])
            acum = acum + (d1 * d2)
            i = i + 1
        return acum/i

    def calcular_correlacion_cruzada(self, BTC, ETH, taumin, taumax, crecimientotau):
        arreglo = [[0,0], 
                   [0,0], 
                   [0,0], 
                   [0,0], 
                   [0,0]]
        max_correlacion = 0
        fila_sol = 0
        tausol = 0
        tau = taumin
        dato1 = BTC
        dato2 = ETH
        i = 0
        while (tau <= taumax):
            acc = 0
            max_correlacion = 0
            acc = self.calcular_correlacion(dato1, dato2, tau)
            if acc > max_correlacion:
                max_correlacion = acc
                tausol = tau
            tau = tau + crecimientotau
            arreglo[i] = max_correlacion, tausol
            i = i + 1
        return arreglo
