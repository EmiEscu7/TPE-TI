from builtins import bytes
#from bitstring import BitArray

length = 24
BUFFER_LENGTH = 8

class Encoder():

    def econde_sequence(self, codigo):
        result = bytearray()

        buffer = 0
        buffer_pos = 0
        #list_idx = 0

        i = 0
        while(i<len(codigo)):
            buffer = buffer << 1 #pongo un 0
            buffer_pos += 1
            if(codigo[i] == '1'):
                buffer = buffer | 1
            
            if(buffer_pos == BUFFER_LENGTH):            
                result.append(buffer)
                buffer = 0
                buffer_pos = 0
            
            i += 1

        if((buffer_pos < BUFFER_LENGTH) and (buffer_pos != 0)):
            while(buffer_pos != BUFFER_LENGTH):
                buffer = buffer << 1
                buffer_pos += 1
            result.append(buffer)
        
        return result


#NO TOCAR!!!!
class Decoder():


    def decode_elements(self, codigo):
        tam = int(codigo.read(1).hex(), base=16)
        tam = str(tam) + int(codigo.read(2).hex(), base=16)
        tam = int(tam)

        cant = 0
        probabilidad = [[], []]
        i = 3
        while(cant<tam):
            elemneto = int(codigo.read(i).hex(), base=16)
            i += 1
            elemneto = str(tam) + int(codigo.read(i).hex(), base=16)
            i += 1
            elemento = int(elemento)
            prob = int(codigo.read(i).hex(), base=16) / tam
            probabilidad[0][i] = elemento
            probabilidad[1][i] = prob
            cant += 1
        return [probabilidad, i]

    def decode_sequence(self, length):
        restore = ""
        file = open("btcfile.bin", "rb")
        global_idx = 0
        mask = 128 #las operacoines con byte/bits (&, |, ^, ~) trabajan con enteros
        buffer_pos = 0        
        read = True

        

        while(global_idx < length):
            if(read):
                dato = int(file.read(i).hex(), base=16)
            

            if(dato > 255):
                dato = dato.to_bytes(2, 'big').hex()
                buffer = int(dato[:2], base=16)
                dato = int(dato[2:], base=16)
                read = False
            else:
                buffer = dato
                read = True
            
            while(buffer_pos < BUFFER_LENGTH):
                if((buffer & mask) == mask):
                    restore += '1'
                else:
                    restore += '0'

                #lo paso a binario para poder descartar el primer bit 
                #ya que en este caso buffer puede contener mas de 8 bits
                buffer = bin(buffer).lstrip('0b')
                if(len(buffer)==8):
                    buffer = int(buffer[1:], base=2) << 1
                elif(len(buffer)==0):
                    buffer = 0
                else:
                    buffer = int(buffer, base=2) << 1

                buffer_pos += 1
                global_idx += 1

                if(global_idx == length):
                    break
            buffer_pos = 0
            i += 1
        
        return restore

#dataBTC = open("BTC.txt", 'r').readlines()
#dataETH = open("ETH.txt", 'r').readlines()
cod = "11100010100011100010001100100001"
encoder = Encoder()

result = encoder.econde_sequence(cod)
print(result)


