from time import sleep

""" Prevenção de Erros """

# s = Stack() 
# s.peek()
# s.push(1)
# s.push(2)
# s.peek()
# while not s.isEmpty():
#     print(s.pop())


""" Remoção de Caracteres com Deque """
# string = input()
# fila = Deque()
# for ch in string:
#     if ch.isalpha() or ch.isspace() or ch in '=-_&¨%$#@!.,><|\;:?°ºª[](){/}':
#         fila.addFront(ch)
#     elif ch.isnumeric():
#         fila.addRear(ch)
#     elif ch == '*':
#         front = fila.removeFront()
#         if front:
#             print(front, end='')
#     elif ch == '+':
#         rear = fila.removeRear()
#         if rear:
#             print(rear,end='')
# print(fila)

""" Separador de Palavras e Números """
# string = input().split()


# palavras = Stack()
# numeros = Stack()
# dicionario = dict()
# for ch in string:
#     if ch.isalpha():
#         palavras.push(ch)
#     elif ch.isnumeric():
#         numeros.push(ch)


# print('Palavras:')
# while not palavras.isEmpty():
#     print(palavras.pop())
# print('\nNumeros:')
# while not numeros.isEmpty():
#     print(numeros.pop())

""" Prioridades"""
# string = input().split()
# num = int(input())

# atividades = Queue()
# peso = Queue()
# for i in string:
#     if i.isalpha():
#         atividades.enqueue(i)
#     else:
#         peso.enqueue(int(i))

# filaPrioridades = Queue()
# auxQueue = Queue()
# while not atividades.isEmpty():
#     if filaPrioridades.isEmpty():
#         filaPrioridades.enqueue((atividades.dequeue(), peso.dequeue()))
        
#     elif filaPrioridades.peek()[1] > peso.peek():
#         while not filaPrioridades.isEmpty():
#             auxQueue.enqueue(filaPrioridades.dequeue())
#         filaPrioridades.enqueue((atividades.dequeue(), peso.dequeue()))
        
#         while not auxQueue.isEmpty():
#             filaPrioridades.enqueue(auxQueue.dequeue())
#     elif filaPrioridades.peek()[1] == peso.peek():
#         while not filaPrioridades.isEmpty():
#             auxQueue.enqueue(filaPrioridades.dequeue())
        
#         while not auxQueue.isEmpty():
#             if auxQueue.peek()[1] == peso.peek():
#                 filaPrioridades.enqueue(auxQueue.dequeue())
#                 filaPrioridades.enqueue((atividades.dequeue(), peso.dequeue()))
#             else:
#                 filaPrioridades.enqueue(auxQueue.dequeue())

#         while not auxQueue.isEmpty():
#             filaPrioridades.enqueue(auxQueue.dequeue())    
#     else:
#          filaPrioridades.enqueue((atividades.dequeue(), peso.dequeue()))

# while num > 0:
#     filaPrioridades.dequeue()
#     num -= 1

# print(f'Tamanho da fila: {filaPrioridades.size()}')
# while not filaPrioridades.isEmpty():
#     aux = filaPrioridades.dequeue()
#     print(f'Atividade: {aux[0]}, Prioridade: #{aux[1]}')


# class NewFila(Queue):
#     def __init__(self, chave=Queue(), valor=Queue()):
#         self.chave = chave
#         self.valor = valor
#         self.prioridades = Queue()

#     def setValor(self, item):
#         self.prioridades.enqueue(item)
    
#     def getChave(self):
#         return self.chave.getItems()

#     def getValor(self):
#         return self.valor.getItems()

#     def priorit(self):
#         atividade = self.getValor()
#         peso = self.getChave()
#         atividade.reverse()
#         peso.reverse()

#         while len(peso)>0:
#             maiorPrioridade = peso.index(min(peso))
#             self.setValor((atividade.pop(maiorPrioridade), peso.pop(maiorPrioridade)))

#         return self.prioridades
    
    
# filaPrioridades = NewFila(peso, atividades)

# while num > 0:
#     filaPrioridades.priorit().dequeue()
#     num -= 1

# print(f'Tamanho da fila: {filaPrioridades.priorit().size()}')
# while not filaPrioridades.priorit().isEmpty():
#     aux = filaPrioridades.priorit().dequeue()
#     print(f'Atividade: {aux[0]}, Prioridade: #{aux[1]}')