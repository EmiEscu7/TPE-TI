BUFFER_LENGTH = 8

def econde_sequence(codigo):
    result = []#bytearray()

    buffer = 0
    buffer_pos = 0

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
    
    retorno = bytearray(result)
    return retorno


def decode_sequence(length):
    restore = ""
    file = open("bytefile.bin", "rb")
    global_idx = 0
    mask = 128 #las operacoines con byte/bits (&, |, ^, ~) trabajan con enteros
    buffer_pos = 0        
    read = True
    i = 1
    

    while(global_idx < length-1):
        #if(read):
        buffer = int(file.read(i).hex(), base=16)
        

        """if(dato > 255):
            dato = dato.to_bytes(2, 'big').hex()
            buffer = int(dato[:2], base=16)
            dato = int(dato[2:], base=16)
            read = False
        else:
            buffer = dato
            read = True"""
        
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

#10111000=184 | 10000100=132 | 01001010=74
result = econde_sequence("101110001000010001001010") 
print(result)
"""arch = open("bytefile.bin", "wb")
arch.write(result)
arch.close()
restore = decode_sequence(23)
print(restore)"""
