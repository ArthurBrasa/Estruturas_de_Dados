"""
Implemente a função frequencia, que recebe uma
 mensagem e retorna o caracter mais comum dessa
  mensagem. Em caso de empate, retorne o primeiro caracter mais frequente"""
string = 'Uma sequencia qualquer'

def frequencia(value):
    letra = ''
    maior = 0
    for letter in value:
      if value.count(letter) > maior:
        letra = letter
        maior = value.count(letter)
    return letra


print(frequencia(string))
