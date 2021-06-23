from TPE1 import *
from TPE2 import *
from TPE3 import *
from encoder_decoder import *

import random
import sys
import numpy as np
import linecache
import math
import matplotlib.pyplot as plt 

class TPE:

    dataBTC = open("BTC.txt", 'r').readlines()
    dataETH = open("ETH.txt", 'r').readlines()
    matriz_pasaje_BTC = None

    #def __init__(self, dataBTC, dataETH):
    #    self.dataBTC = dataBTC
    #    self.dataETH = dataETH
    

    def ejercicio1(self):
        #GENERO EL OBJETO QUE RESUELVE EL EJERCICIO
        ej1 = TPE1()

        """A PARTIR DE ACA SE CALCULAN LAS MATRICES DE PASAJE DE BTC Y ETH.
        EJERCICIO 1A"""
        matrix = ej1.calcular_matriz_pasaje(self.dataBTC)
        self.matriz_pasaje_BTC = matrix
        print('MATRIZ DE PASAJE BTC:')
        self.print_matrix(matrix)
        print("\n")
        print("\n")

        matrix = ej1.calcular_matriz_pasaje(self.dataETH)
        self.matriz_pasaje_ETH = matrix
        print('MATRIZ DE PASAJE ETH:')
        self.print_matrix(matrix)
        print("\n")
        print("\n")

        """A PARTIR DE ACA SE CALCULA LA AUTOCORRELACION DE CADA MONEDA. 
        EJERCICIO 1B"""
        autocorrelation = ej1.calcular_autocorrelacion(self.dataBTC, 1, 50)
        print('AUTOCORRELACION DE LA MONEDA BTC:')
        self.print_array(autocorrelation)
        self.plot(autocorrelation, 50, "AUTOCORRELACION DEL BTC", "Autocorrelacion", "Tau")
        print("\n")
        print("\n")

        autocorrelation = ej1.calcular_autocorrelacion(self.dataETH, 1, 50)
        print('AUTOCORRELACION DE LA MONEDA ETH:')
        self.print_array(autocorrelation)
        self.plot(autocorrelation, 50, "AUTOCORRELACION DEL ETH", "Autocorrelacion", "Tau")
        print("\n")
        print("\n")

        """A PARTIR DE ACA SE CALCULA LA AUTOCORRELACION DE CADA MONEDA. 
        EJERCICIO 1C"""
        cross_correlation = ej1.calcular_correlacion_cruzada(self.dataBTC, self.dataETH, 0, 200, 50)
        print('CORRELACION CRUZADA ENTRE BTC Y ETH:')
        self.print_matrix(cross_correlation)
        crossCorrelation = []
        for fila in cross_correlation:
            crossCorrelation.append(fila[0])
        self.plot(crossCorrelation, 5, "CORRELACION CRUZADA ENTRE BTC Y ETH", "Correlacion Cruzada", "Tau")
        print("\n")
        print("\n")

    def ejercicio2(self):
        #GENERO EL OBJETO QUE RESUELVE EL EJERCICIO 2
        ej2 = TPE2()
        encoder = Encoder()
        decoder = Decoder()

        """A PARTIR DE ACA SE CALCULA LA DISTRIBUCION DE PROBABILIDADES DE LA MONEDA BTC Y ETH
        EJERCICIO 2A"""
        distribBTC = ej2.distribucion_probabilidad(self.dataBTC)
        print("DISTRIBUCION DEL BITCOIN:")
        self.print_dict(distribBTC)
        print("\n")
        print("\n")


        distribETH = ej2.distribucion_probabilidad(self.dataETH)
        print("DISTRIBUCION DEL BITCOIN:")
        self.print_dict(distribETH)
        print("\n")
        print("\n")


        """A PARTIR DE ACA SE GENERA LA CODIFICACION DE LA FUENTE BTC Y ETH MEDIANTE HUFFMAN SEMI-ESTATICO
        EJERCICIO 2B"""
        huffmanBTC = ej2.get_codification(self.dataBTC, distribBTC) #obtengo el codigo de la fuente BTC con huffman semi estatico
        cabeceraBTC = ej2.get_cabecera(distribBTC, len(self.dataBTC))
        huffmanBTC_bin = encoder.econde_sequence(huffmanBTC)
        #cabeceraBTC_bin = encoder.econde_sequence(cabeceraBTC)
        #print(cabeceraBTC_bin)
        #final_code = cabeceraBTC + codBTC_bin
        print("CODIGO HUFFMAN SEMI-ESTATICO PARA LA FUENTE BTC:")
        print(str(cabeceraBTC) + "   |   " + str(huffmanBTC))
        self.save_file("huffmanBTC", huffmanBTC_bin, cabeceraBTC)
        print("\n")
        print("\n")


        """
            DECODIFICACION DE HUFFMAN BTC
        
        [restored, restored_header] = decoder.decode_sequence("huffmanBTC", len(huffmanBTC), True)
        print("CODIGO DECODIFICADO HUFFMAN SEMI-ESTATICO PARA LA FUENTE BTC:")
        print(str(restored_header) + "   |   " + str(restored))
        """


        huffmanETH = ej2.get_codification(self.dataETH, distribETH) #obtengo el codigo de la fuente ETH con huffman semi estatico
        cabeceraETH = ej2.get_cabecera(distribETH, len(self.dataETH))
        huffmanETH_bin = encoder.econde_sequence(huffmanETH)
        #cabeceraETH_bin = encoder.econde_sequence(cabeceraETH)
        print("CODIGO HUFFMAN SEMI-ESTATICO PARA LA FUENTE ETH:")
        print(str(cabeceraETH) + "   |   " + str(huffmanETH))
        self.save_file("huffmanETH", huffmanETH_bin, cabeceraETH)
        print("\n")
        print("\n")

        """A PARTIR DE ACA SE GENERA LA CODIFICACION DE LA FUENTE BTC Y ETH MEDIANTE RLC
        EJERCICIO 2C"""
        [rlcBTC, rlcBTC_para_ver] = ej2.get_RLC_coding(self.dataBTC) #obtengo el codigo de la fuente BTC con RLC
        rlcBTC_bin = encoder.econde_sequence(rlcBTC)
        print("CODIGO RLC PARA LA FUENTE BTC:")
        print(rlcBTC_para_ver)
        self.save_file("rlcBTC", rlcBTC_bin)
        print("\n")
        print("\n")

        [rlcETH, rlcETH_para_ver] = ej2.get_RLC_coding(self.dataETH) #obtengo el codigo de la fuente BTC con RLC
        rlcETH_bin = encoder.econde_sequence(rlcETH)
        print("CODIGO RLC PARA LA FUENTE ETH:")
        print(rlcETH_para_ver)
        self.save_file("rlcETH", rlcETH_bin)
        print("\n")
        print("\n")

    
    def ejercicio3(self):
        ej3 = TPE3()

        """ A PARTIR DE ACA SE CALCULA EL CANAL ASOCIADO A LAS 2 MOENDAS.
        EJERCICIO 3A """
        PasajeBTC = ej3.calcularPasajeMoneda(self.dataBTC)
        PasajeETH = ej3.calcularPasajeMoneda(self.dataETH)
        Probs = ej3.get_probabilities(self.matriz_pasaje_BTC)
        Canal = ej3.calcularCanal(self.dataBTC, PasajeBTC, PasajeETH, Probs)
        print("\n")
        print("EL CANAL ASOCIADO ES EL SIGUIENTE:")
        self.print_matrix(Canal)
        print("\n")
        print("\n")



        """ A PARTIR DE ACA SE CALCULAN EL RUIDO Y LA PERDIDA DEL CANAL ASOCIADO.
        EJERCICIO 3B """
        probsBTC = ej3.get_probabilities(self.matriz_pasaje_BTC)
        print("\n")
        probsETH = ej3.get_probabilities(self.matriz_pasaje_ETH)
        ruido = ej3.get_ruido_canal(probsBTC, Canal)        
        print("EL RUIDO DEL CANAL ASOCIADO ES: " + str(ruido))
        print("\n")
        print("\n")
        prob_cond = ej3.calcularCanal(self.dataBTC, PasajeETH, PasajeBTC, Probs)
        perdida = ej3.get_perdida_canal(probsETH, prob_cond)
        print("LA PERDIDA DEL CANAL ASOCIADO ES: " + str(perdida))



    def save_file(self, name, codigo, cabecera=None):
        name += ".bin"
        if(cabecera != None):
            file = open(name, "w")
            file.write(cabecera)
            file.close()
        file = open(name, "wb")
        file.write(codigo)
        file.close()

    def print_array(self, array):
        for valor in array:
            print("\t", valor)


    def print_matrix(self, matrix):
        for fila in matrix:
            for valor in fila:
                print("\t", valor, end= " ")
            print()

    def print_dict(self, dict):
        for key, value in dict.items():
            print(str(key)+": "+str(value))

    def plot(self, to_plot, max, title, ylabel, xlabel):
        plt.plot(range(max), to_plot)
        plt.plot()
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
        plt.show()

test = TPE()

test.ejercicio1()

print("PRESS ENTER TO CONTINUE TO CODIFICATION & COMPRESSION!!!")
while(True):
    i = input()
    if not i:
        break


test.ejercicio2()

print("PRESS ENTER TO CONTINUE TO CHANNELS!!!")
while(True):
    i = input()
    if not i:
        break


test.ejercicio3()

print("PRESS ENTER TO FINISH!!!")
while(True):
    i = input()
    if not i:
        break

