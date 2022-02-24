class Stack():
    def __init__(self):
        self.items = []
    
    def __str__(self) -> str:
        return str(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            return None
        
    def size(self):
        return len(self.items)

total = int(input())
pilha = Stack()
while total>0:
    expressao = input()
    for c in expressao:
        print(c)

    total -= 1