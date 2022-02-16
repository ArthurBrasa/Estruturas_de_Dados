# from timeit import Timer
# def solucaoAnagrama4(s1,s2):
#     c1 = [0]*26
#     c2 = [0]*26

#     for i in range(len(s1)):
#         pos = ord(s1[i])-ord('a')
#         c1[pos] = c1[pos] + 1

#     for i in range(len(s2)):
#         pos = ord(s2[i])-ord('a')
#         c2[pos] = c2[pos] + 1

#     j = 0
#     aindaOK = True
#     while j<26 and aindaOK:
#         if c1[j]==c2[j]:
#             j = j + 1
#         else:
#             aindaOK = False

#     return aindaOK

# print(solucaoAnagrama4('marrocos','socorram'))

# def teste1():
#     l = []
#     for i in range(1000):
#         l = l + [i]

# def teste2():
#     l = []
#     for i in range(1000):
#         l.append(i)

# def teste3():
#     l = [i for i in range(1000)]

# def teste4():
#     l = list(range(1000))

# t1 = Timer("teste1()", "from __main__ import teste1")
# print("concatenacao ",t1.timeit(number=1000), "milissegundos")
# t2 = Timer("teste2()", "from __main__ import teste2")
# print("append ",t2.timeit(number=1000), "milissegundos")
# t3 = Timer("teste3()", "from __main__ import teste3")
# print("comprehension ",t3.timeit(number=1000), "milissegundos")
# t4 = Timer("teste4()", "from __main__ import teste4")
# print("range ",t4.timeit(number=1000), "milissegundos")
# print('\n\n')

# t1 = Timer("teste1()", "from __main__ import teste1")
# print("concatenacao ",t1.timeit(number=1000), "milissegundos")
# t2 = Timer("teste2()", "from __main__ import teste2")
# print("append ",t2.timeit(number=1000), "milissegundos")
# t3 = Timer("teste3()", "from __main__ import teste3")
# print("comprehension ",t3.timeit(number=1000), "milissegundos")
# t4 = Timer("teste4()", "from __main__ import teste4")
# print("range ",t4.timeit(number=1000), "milissegundos")

""" Estudo do tempo de execução do pop() e pop(0):"""

# popzero = Timer("x.pop(0)",
#                 "from __main__ import x")
# popfim = Timer("x.pop()",
#                "from __main__ import x")
# print("pop(0)             pop()")
# for i in range(1000000,100000001,1000000):
#     x = list(range(i))
#     pt = popfim.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" %(pz,pt))

# import timeit
# import random

# """ Usando Dicionarios:"""

# for i in range(10000,1000001,20000):
#     t = timeit.Timer("random.randrange(%d) in x"%i,
#                      "from __main__ import random,x")
#     x = list(range(i))
#     tempo_lista = t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     tempo_dic = t.timeit(number=1000)
#     print("%d,%10.3f,%10.3f" % (i, tempo_lista, tempo_dic))

