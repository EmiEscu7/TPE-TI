from TPE1 import *

import random
import sys
import numpy as np
import linecache
import math
import matplotlib.pyplot as plt 

class TPE:

    dataBTC = open("BTC.txt", 'r').readlines()
    dataETH = open("ETH.txt", 'r').readlines()

    #def __init__(self, dataBTC, dataETH):
    #    self.dataBTC = dataBTC
    #    self.dataETH = dataETH
    

    def ejercicio1(self):
        #GENERO EL OBJETO QUE RESUELVE EL EJERCICIO
        ej1 = TPE1()

        """A PARTIR DE ACA SE CALCULAN LAS MATRICES DE PASAJE DE BTC Y ETH.
        EJERCICIO 1A"""
        matrix = ej1.calcular_matriz_pasaje(self.dataBTC)
        print('MATRIZ DE PASAJE BTC:')
        self.print_matrix(matrix)

        matrix = ej1.calcular_matriz_pasaje(self.dataETH)
        print('MATRIZ DE PASAJE ETH:')
        self.print_matrix(matrix)

        """A PARTIR DE ACA SE CALCULA LA AUTOCORRELACION DE CADA MONEDA. 
        EJERCICIO 1B"""
        autocorrelation = ej1.calcular_autocorrelacion(self.dataBTC, 1, 50)
        print('AUTOCORRELACION DE LA MONEDA BTC:')
        self.print_array(autocorrelation)
        self.plot(autocorrelation, 50, "AUTOCORRELACION DEL BTC", "Autocorrelacion", "Tau")

        autocorrelation = ej1.calcular_autocorrelacion(self.dataETH, 1, 50)
        print('AUTOCORRELACION DE LA MONEDA ETH:')
        self.print_array(autocorrelation)
        self.plot(autocorrelation, 50, "AUTOCORRELACION DEL ETH", "Autocorrelacion", "Tau")

        """A PARTIR DE ACA SE CALCULA LA AUTOCORRELACION DE CADA MONEDA. 
        EJERCICIO 1C"""
        cross_correlation = ej1.calcular_correlacion_cruzada(self.dataBTC, self.dataETH, 0, 200, 50)
        print('CORRELACION CRUZADA ENTRE BTC Y ETH:')
        self.print_matrix(cross_correlation)
        crossCorrelation = []
        for fila in cross_correlation:
            crossCorrelation.append(fila[0])
        self.plot(crossCorrelation, 5, "CORRELACION CRUZADA ENTRE BTC Y ETH", "Correlacion Cruzada", "Tau")



    def print_array(self, array):
        for valor in array:
            print("\t", valor)


    def print_matrix(self, matrix):
        for fila in matrix:
            for valor in fila:
                print("\t", valor, end= " ")
            print()

    def plot(self, to_plot, max, title, ylabel, xlabel):
        plt.plot(range(max), to_plot)
        plt.plot()
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
        plt.show()

test = TPE()

test.ejercicio1()
