
total = int(input())
string = input()
lista = []
for c in string:
    lista.append(c)

for c in lista:
    if c == '0':
        lista.pop(0)
    else:
        lista.pop(0)
        break

lista.reverse()
for c in lista:
    if c == '0':
        lista.pop(0)
    else:
        lista.pop(0)
        break

print(lista)