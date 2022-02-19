# from time import sleep

class Queue:
    def __init__(self):
        self.items = []

    def getItems(self):
        return self.items
    
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


""" Exemplo HotPotato"""

# def hotPotato(listName, num):
#     fila = Queue()
#     for name in listName:
#         fila.enqueue(name)
    
#     while fila.size() > 1:
#         for i in range(num):
#             fila.enqueue(fila.dequeue())
#         fila.dequeue()

#     return fila.dequeue()    

# nomesLista = ['Arthur', 'Marcos', 'Maria', 'Sakura', 'Naruto', 'Covid-19']


# if __name__ == '__main__':
#     print(hotPotato(nomesLista, 5))
