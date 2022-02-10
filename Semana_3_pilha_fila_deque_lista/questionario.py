from stack import Stack

""" Prevenção de Erros """

s = Stack() 
s.peek()
s.push(1)
s.push(2)
s.peek()
while not s.isEmpty():
    print(s.pop())


""""""