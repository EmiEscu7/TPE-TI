from encoder_decoder import *

class Nodo():

    def __init__(self, clave=None, prob=None, izq=None, der=None):
        self.der = der
        self.izq = izq
        self.probabilidad = prob
        self.clave = clave    
    

    def __lt__(self, other):
        return self.getProb() <= other.getProb()

    def getClave(self):
        return self.clave

    def getProb(self):
        return self.probabilidad
    
    def getIzq(self):
        return self.izq

    def getDer(self):
        return self.der


class TPE2():

    def distribucion_probabilidad(self, moneda):
        dict = {}
        i = 0
        tam = len(moneda)
        while (i < tam):
            dato = int(moneda[i])
            if (dato in dict):
                dict[dato] += 1
            else:
                dict.update({dato: 1})
            i = i + 1
        for key, value in dict.items():
            dict[key] = value/tam
        return dict
    
    def getNodos(self, dict_prob):
        nodos = []
        for key, value in dict_prob.items():
            nodo = Nodo(key, value)
            nodos.append(nodo)
        return nodos

    def get_codigo(self, nodo, cod, codigos):
        if(nodo.getIzq() != None):
            cod += "0"
            self.get_codigo(nodo.getIzq(), cod, codigos)
            cod = cod[:-1]
        
        if(nodo.getDer() != None):
            cod += "1"
            self.get_codigo(nodo.getDer(), cod, codigos)
            cod = cod[:-1]
        
        if((nodo.getIzq() == None) and (nodo.getDer() == None)):
            n_cod = cod
            del cod
            codigos.update({nodo.getClave(): n_cod})

    def calcular_huffman_semiestatico(self, dict_prob):
        #orden_real = prob
        #prob.sort()  
        nodos = self.getNodos(dict_prob)

        val_nodo1 = nodos[0].getProb()
        val_nodo2 = nodos[1].getProb()
        
        while(val_nodo1 + val_nodo2 != 1):
            nodo1 = nodos.pop(0)
            nodo2 = nodos.pop(0)
            suma = round(nodo1.getProb() + nodo2.getProb(), 3)
            new_nodo = Nodo(prob=suma, izq=nodo1, der=nodo2)
            nodos.append(new_nodo)
            nodos.sort()
            val_nodo1 = nodos[0].getProb()
            val_nodo2 = nodos[1].getProb()
        
        nodo1 = nodos.pop(0)
        nodo2 = nodos.pop(0)
        raiz = Nodo(prob=(val_nodo1 + val_nodo2), izq=nodo1, der=nodo2)
        return raiz

    def get_codification(self, fuente, dict_prob):

        #armo el arbol y obtengo la raiz
        raiz = self.calcular_huffman_semiestatico(dict_prob) 
        codigos = {}
        cod = ""
        self.get_codigo(raiz, cod, codigos) #genero el codigo para cada valor
        
        i = 0
        tam = len(fuente)
        retorno = ""
        #empiezo a generar el codigo de la fuente
        while(i < tam):
            valor = int(fuente[i])
            retorno += str(codigos[valor])
            i += 1
        return retorno
  
    def get_cabecera(self, dict_prob, tam):
        cabecera = ""
        tam_bit = tam.to_bytes(4, "big")
        cabecera += str(tam_bit)

        for key, value in dict_prob.items():
            dato = key.to_bytes(4, "big")
            cabecera += str(dato)
            cant = int(value * tam).to_bytes(4, "big")
            cabecera += str(cant)
    
        return cabecera

    def get_RLC_coding(self, fuente):

        codigo = ""
        cod_para_ver = ""
        simb_act = int(fuente[0])
        cant_act_simb = 1
        i = 1
        tam = len(fuente)

        while (i < tam):
            s = int(fuente[i])
            if(s == simb_act):
                cant_act_simb += 1
            else:
                codigo += str(simb_act) + str(cant_act_simb)
                cod_para_ver += "(" + str(simb_act) + "-" + str(cant_act_simb) + ") -- "
                simb_act = s
                cant_act_simb = 1
            i += 1
        
        return [codigo, cod_para_ver[:-3]]
