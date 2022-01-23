# recebendo dados
def format_xy(x_y):
    x, y = float(x_y[0]), float(x_y[1])
    return (x, y)

def distancia(point_1, point_2):
    distancia = ((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)**0.5
    return distancia


def holes():
    posicao = {}
    holes = int(input())
    rabbit = input().split()
    posicao['rabbit'] = format_xy(rabbit)
    fox = input().split()
    posicao['fox'] = format_xy(fox)
    lista = []
    while holes>0:
        lista.append(format_xy(input().split()))
        holes -= 1
    posicao['holes'] = lista
    return posicao


def run_for_your_life(coordenadas):
    for buraco in coordenadas.get('holes'):
        distancia_coelho = distancia(coordenadas['rabbit'], buraco)
        distancia_raposa = distancia(coordenadas['fox'], buraco)
        
        if distancia_coelho < distancia_raposa/2:
            return f'O coelho pode escapar pelo buraco ({buraco[0]:.3f}, {buraco[1]:.3f}).'
        
    return 'O coelho nao pode escapar.'

posicao = holes()
print(run_for_your_life(posicao))
