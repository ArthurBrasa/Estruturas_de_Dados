
def invert_string(text):
    return text[::-1]

def remover_0_laterais(text):
    text = text[text.find('1'):]
    text = invert_string(text)
    return invert_string(text[text.find('1'):])

def cont_zeros(text):
    if len(text) == 1:
        return 0
    return text.count('0')


n = int(input())
while n > 0:
    texto = input()
    texto = cont_zeros(remover_0_laterais(texto))
    print(texto)
    n -= 1
