# import time

# num_testes = 5
# media = 0

# for _ in range(num_testes):
#     inicio = time.time()
#     soma_ate(10000)
#     fim = time.time()
    
#     tempo_de_execucao = fim - inicio
#     media += tempo_de_execucao
#     print(f'Tempo: {tempo_de_execucao}')

# media /= num_testes
# print(f'Média de tempo: {media}')

"""n eh um numero inteiro positivo"""
# def funcao(n): 
#     aux = 0 
#     for i in range(1, n+1): 
#         j = 1
#         while j < i:
#             j = j*2  
#             aux = aux + i 
#     return aux

# print(funcao(10000000))

"""L é uma lista ordenada e val é um elemento"""
# def busca(L, val): 
#     achou = False
#     comeco = 0
#     meio = 0
#     fim = len(L) - 1
#     while comeco <= fim: 
#         meio = (fim + comeco) // 2
#         if L[meio] < val: 
#             comeco = meio + 1
#         elif L[meio] > val: 
#             fim = meio - 1
#         else:
#             achou = True
#             return achou, meio 
#     return achou, -1

"""L eh uma lista de tamanho n e val eh um elemento"""
# def busca(L, val):
#     achou = False
#     i = 0
#     for ele in L:
#         if(ele == val):
#             achou = True
#             return achou, i
#         i += 1
#     return achou, -1