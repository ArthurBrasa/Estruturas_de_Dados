class Queue:
    def __init__(self, fila=[]):
        self.items = fila

    def getItems(self):
        return self.items[:]
    
    def isEmpty(self):
        return self.items == []

    def __str__(self) -> str:
        return str(self.items)

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        try:
            return self.items.pop()
        except:
            return None
    
    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            pass

    def size(self):
        return len(self.items)


def mostraFila(fila, string):
    f = fila
    print(string)
    for i in range(0, f.size()):
        idade = f.dequeue()
        if type(idade) != int:
            print(f'{idade[1]} - {idade[0]}')
        else:
            print(f'{i+1} - {idade}')

        f.enqueue(idade)

def especial(fila):
    filaEspecial = Queue()
    aux = Queue(fila)
    for i in range(0, aux.size()):
        idade = aux.dequeue()
        if idade >= 60:
            filaEspecial.enqueue((idade, i+1))
    return filaEspecial

filaOriginal = Queue()
idade = 0
while idade!='':
    idade = input()
    if idade == '':
        continue
    filaOriginal.enqueue(int(idade))

mostraFila(filaOriginal, 'Fila geral original')
filaEspecial = especial(filaOriginal.getItems())
print()
