"""
Números primos gêmeos são pares de números primos 
(p1, p2) tais que p2=p1+2.=
Implemente uma função chamada primos_gemeos que r
ecebe um número inteiro n e retorna os n primeiros
 pares de números pr
imos gêmeos, conforme formatação indicada abaixo.
"""

def eh_gemeo(p1, tupla=False):
    if tupla:
        return  (p1, p1 + 2)
    else:
        p2 = p1 + 2
    
    if eh_primo(p2):
        return True
    else:
        return False

def eh_primo(num):
    if num == 2 or num == 3 or num == 5:
        return True
    else:
        for n in range(2, num):
            if num%n == 0:
                return False
        return True
    


def primos_gemeos(value):
    numeros_primos = []
    cont = 2
    while len(numeros_primos)<value:
        cont += 1
        if eh_primo(cont):
            if eh_gemeo(cont):
                numeros_primos.append(eh_gemeo(cont, True))
    return numeros_primos

print(primos_gemeos(80))
