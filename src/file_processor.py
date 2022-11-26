"""
Métodos utilitários para processamento de arquivos
"""


def read(file):
    print('')
    print('Realizando leitura do arquivo de entrada')

    return read_file(file)


def read_file(file):
    with open(file, 'r') as f:
        file_content = []

        for line in f:
            file_content.append([int(x) for x in line.split(',')])

    print('Inspecionando dados obtidos do arquivo de entrada')
    print(file_content)
    print('')

    return file_content


def soma(a, b):
    return a + b
