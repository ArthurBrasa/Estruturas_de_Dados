

elementos = int(input())
listaElementos = input().split()
novaListaElementos = list()
for num in listaElementos:
    novaListaElementos.append(int(num))
tamanhoJanela = int(input())

comeco = 0

while tamanhoJanela <= elementos:
    nums = novaListaElementos[comeco:tamanhoJanela]
    print(max(nums), end='  ')
    tamanhoJanela +=1
    comeco+=1
