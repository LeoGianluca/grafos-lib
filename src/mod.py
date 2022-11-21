
def soma(a, b):
    return a + b


def read_matrix(file):
    print('Lendo matriz')
    with open(file, 'r') as f:
        matriz = []
        for line in f:
            matriz.append([int(x) for x in line.split(',')])
    return matriz


def read_list(file):
    print('Lendo lista')
    with open(file, 'r') as f:
        lista = []
        for line in f:
            lista.append([int(x) for x in line.split(',')])
    return lista
