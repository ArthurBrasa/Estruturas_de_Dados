class Deque:
    def __init__(self):
        self.items = []
    
    def __str__(self) -> str:
        return str(self.items)

    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        try:
            return self.items.pop()
        except:
            return None
        
    def removeRear(self):
        try:
            return self.items.pop(0)
        except:
            return None
        
    def size(self):
        return len(self.items)


""" EXEMPLO 1"""
# palíndromo

# def palchecker(aString):
#     charDeque = Deque()

#     for ch in aString:
#         charDeque.addRear(ch)

#     stillEqual = True
#     while charDeque.size() > 1 and stillEqual:
#         first = charDeque.removeFront()
#         last = charDeque.removeRear()
#         if first != last:
#             stillEqual = False
#     return stillEqual


# if __name__ == "__main__":
#     print(palchecker("lsdkjfskf"))
#     print(palchecker("radar"))
