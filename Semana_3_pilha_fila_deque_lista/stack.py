""" Implementação de uma Pilha - Stack _ FILO  """

class Stack():
    def __init__(self):
        self.items = []

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




# EXEMPLO PRATICO 1 RETIRADO DO LIVRO "Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python"
# from pythonds.basic.stack import Stack
"""  Parênteses Balanceados """
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False



""" Exemplo Pratico 2"""
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)



"""Exemplo pratco 3"""

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

# print(divideBy2(42))

"""Exemplo pratco 4"""

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEFGHIJKL"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString



if __name__ == "__main__":
    myStack = Stack()
    print(myStack.isEmpty())
    myStack.push('Hamburguer')
    myStack.push('Juice')
    myStack.push('Milk Shake')
    print(myStack.size())
    print(myStack.pop())
    print(myStack.peek())
    
    print(parChecker('((()))'))
    print(parChecker('(()'))  
    
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))


    print(baseConverter(15,2))
    print(baseConverter(15,16))
    print(baseConverter(25, 8))
    print(baseConverter(256, 16))
    print(baseConverter(26, 26))