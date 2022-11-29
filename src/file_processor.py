"""
Métodos utilitários para processamento de arquivos
"""

import pprint


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

            if line:  # Ignora o processamento em caso de linhas vazias
                file_content.append([str(x) for x in line.split(';')])

    return file_content


def read_file_matrix(file):
    """
    Realiza leitura de um arquivo de matriz de adjacencias.

    :param file: arquivo a ser processado

    :return: representacao do conjunto de arestas do grafo
    """
    with open(file, 'r') as f:
        file_lines = [(line_num, line) for line_num, line in enumerate(f)]
        # matrix = list()

        vertices_colmns = []

        for line in file_lines:
            line_number = line[0]
            line_content = line[1]

            print(f'line_number={line_number}, line_content={line_content}')

            line_content = line_content.rstrip()  # Remove espacos a direita

            line_splited_values = line_content.split(';')

            if line_number == 0:  # Lendo primeira linha com lista de nós em colunas
                for val in line_splited_values:
                    vertices_colmns.append(val)

            values = list()

            for val in line_splited_values:
                values.append(val)

            print(f'values: {values}')
        #     matrix.append(values)

        print(f'vertices_colmns: {vertices_colmns}')

        # row_num = 6
        # col_num = 6
        # adjacency_matrix = []
        #
        # for i in range(row_num):
        #     row = []
        #     for j in range(col_num):
        #         row.append(0)
        #     adjacency_matrix.append(row)
        #
        # edges = [(1, 2), (2, 4), (2, 3), (3, 4), (4, 5), (3, 6), (5, 6)]
        #
        # for edge in edges:
        #     row = edge[0]
        #     col = edge[1]
        #     adjacency_matrix[row - 1][col - 1] = 1
        #     adjacency_matrix[col - 1][row - 1] = 1
        #
        # print("The edges in the graph are:")
        # print(edges)
        # print("The adjacency matrix is:")
        # pprint.pprint(adjacency_matrix)

    # return matrix


def soma(a, b):
    return a + b
