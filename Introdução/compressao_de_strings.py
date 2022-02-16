total_strings = int(input())

def descompressao(string):
    frase = ''
    letra = ''
    num = ''
    for c in string:
        if c.isalpha():
            if num != '':
                frase += letra*int(num)
                num = ''
            letra = c  
        else:
            num += c
    frase += letra*int(num)
    return frase

while total_strings>0:
    print(descompressao(input()))
    total_strings -= 1

