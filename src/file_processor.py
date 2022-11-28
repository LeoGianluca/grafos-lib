"""
Métodos utilitários para processamento de arquivos
"""


def read(file, file_type):
    print(f'Processando arquivo (arquivo={file}, tipo={file_type})')

    if file_type == 'matriz':
        file_content = read_file_matrix(file)
    elif file_type == 'lista':
        file_content = read_file_list(file)
    else:
        print(f'Tipo de arquivo desconhecido [{file_type}]')

    print('')
    print('Inspecionando dados obtidos do arquivo de entrada')
    print(file_content)
    print('')

    return file_content


def read_file_list(file):
    """
    Realiza leitura de um arquivo de lista de adjacencias.

    :param file: arquivo a ser processado

    :return: representacao do conjunto de arestas do grafo
    """
    with open(file, 'r') as f:
        file_content = []

        for line in f.readlines():
            line = line.rstrip()  # Remove espacos a direita

            if line:  # Ignora o processamento de linhas em branco
                file_content.append([str(x) for x in line.split(';')])

    return file_content


def read_file_matrix(file):
    """
    Realiza leitura de um arquivo de matriz de adjacencias.

    :param file: arquivo a ser processado

    :return: representacao do conjunto de arestas do grafo
    """
    with open(file, 'r') as f:
        file_content = []

        for line in f.readlines():
            line = line.rstrip()  # Remove espacos a direita

            if line:  # Ignora o processamento de linhas em branco
                file_content.append([str(x) for x in line.split(';')])

    return file_content


def soma(a, b):
    return a + b
