from math import ceil

def media_transferencia(bytes, arq):
    media = ceil((5*bytes)/arq)
    return media

def calcular_transferencia(bytes):
    print(f'Transmitindo {bytes} bytes...')
    temp = 0
    arq = 0
    temporizador = 0
    while bytes>0:
        temporizador += 1
        transferido = int(input())
        bytes -= transferido
        if bytes == 0:
            temp += 1
            continue
        arq += transferido
        if temporizador == 5:
            if arq == 0:
                print('Tempo restante: pendente...')     
            else:
                print(f'Tempo restante: {media_transferencia(bytes, arq)} segundos.')
                arq = 0
            temporizador = 0
        temp += 1  
    return temp

print(f'Tempo total: {(calcular_transferencia(int(input())))} segundos.')