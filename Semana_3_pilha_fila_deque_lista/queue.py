from time import sleep

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def __str__(self) -> str:
        return str(self.items)

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)


""" Exemplo HotPotato"""

def hotPotato(listName, num):
    fila = Queue()
    for name in listName:
        fila.enqueue(name)
    
    while fila.size() > 1:
        for i in range(num):
            fila.enqueue(fila.dequeue())
        fila.dequeue()

    return fila.dequeue()    

nomesLista = ['Arthur', 'Marcos', 'Maria', 'Sakura', 'Naruto', 'Covid-19']


print(hotPotato(nomesLista, 5))

