"""Lista Comprasa"""
class ListaCompra():
    def __init__(self):
        self.lista = []
        self.listaPreco = []
        self.listaOrdenada = None

    
    def __str__(self):
        return str(self.lista)
    
    def isEmpty(self):
        return self.lista == []
    
    def OrdenadoIsEmpty(self):
        return self.listaOrdenada == []
    
    def getPreço(self):
        return self.listaPreco

    def inserir(self, item, valor):
        self.listaPreco.append(float(valor))
        self.lista.append(item)

    def popItem(self, item):
        self.listaPreco.pop(self.lista.index(item))
        return self.lista.remove(item)

    def ordenar(self):
        ordenado = list()
        while not self.isEmpty():
            menor = self.listaPreco.index(min(self.getPreço()))
            ordenado.append((self.lista.pop(menor), self.listaPreco.pop(menor)))
        self.listaOrdenada = ordenado

    def MostraNaTela(self):
        total = len(self.listaOrdenada)
        soma = 0
        while not self.OrdenadoIsEmpty():
            item = self.listaOrdenada.pop()
            soma += item[1]
            print(f'{item[0]}: R$ {item[1]:.2F}')
        print('----------------------')
        print(f'{total} item(ns): R$ {soma:.2f}')





minhaLista = ListaCompra()
flag = True
while flag:
    valor = input().split()
    if valor[0] == '-':
        minhaLista.popItem(valor[1])
    elif valor[0] == 'fim':
        flag = False
    else:
        minhaLista.inserir(valor[0], valor[1])
    
    
minhaLista.ordenar()
minhaLista.MostraNaTela()