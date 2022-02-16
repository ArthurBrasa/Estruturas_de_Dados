total_jogadores = int(input())
jogadores = input().split()

for i, jogador in enumerate(jogadores):
    jogadores[i] = int(jogador)
    
jogadores.sort()
jogadores.reverse()

titulares = sum(jogadores[:11])
reservas = sum(jogadores[11:22])

print(titulares-reservas)
