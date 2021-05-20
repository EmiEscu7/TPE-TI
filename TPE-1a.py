import random
import sys
import numpy as np
import linecache
import math

def sig_dado_ant(t,moneda):
    archivo = open(moneda)
    s = archivo.readlines()
    return float(s[t])

def prob_condicional(moneda):
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
            j=j+1
        i=i+1
    return retorno


def calcular_autocorrelacion(moneda, tau_min, tau_max):
    autocorrelacion = np.zeros(tau_max+1)
    tau = tau_min
    t_actual = 0
    tamanio = len(dato)

    while(tau <= tau_max):
        

        while (tau + t_actual < tamanio):
            s1 = int(dato[t_actual])
            s2 = int(dato[t_actual+tau])
            t_actual += 1

            autocorrelacion[tau] += s1*s2

        autocorrelacion /= t_actual
        t_actual=0
        tau += 1
    
    return autocorrelacion



dato = open("BTC.txt", "r").readlines()
print ('MATRIZ DE PASAJE BTC')
fuente_BTC = prob_condicional(dato)
s = 0
for i in range(len(fuente_BTC)):
    for j in range(len(fuente_BTC[i])):
        print(fuente_BTC[i][j], end=' ')
    print()
print ('AUTOCORRELACION DE BTC')
print(calcular_autocorrelacion(dato, 1, 50))




print ('MATRIZ DE PASAJE ETH')
dato = open("ETH.txt", "r").readlines()
fuente_ETH = prob_condicional(dato)
s = 0
for i in range(len(fuente_ETH)):
    for j in range(len(fuente_ETH[i])):
        print(fuente_ETH[i][j], end=' ')
    print()
print ('AUTOCORRELACION DE ETC')
print(calcular_autocorrelacion(dato, 1, 50))