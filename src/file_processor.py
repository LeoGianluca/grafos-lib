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
        arestas = []
        vertices_finais = []

        file_lines = [(line_num, line) for line_num, line in enumerate(f)]

        print('')

        for line in file_lines:
            line_number = line[0]
            line_content = line[1]

            line_splited_values = line_content.rstrip().split(';')

            # Processando primeira linha do arquivo,
            # referente ao cabecalho com lista de nós em colunas
            if line_number == 0:
                vertices_finais = line_splited_values
                vertices_finais.pop(0)
                continue

            line_values = list()

            for val in line_splited_values:
                line_values.append(val)

            for idx, val in enumerate(line_values):
                if idx == 0:
                    vertice1 = line_values[0]
                    print(f'Processando conexões para o vértice {vertice1}')  # ignorando primeira valor (rótulo do vértice)
                    continue

                if int(val) > 0:
                    vertice2 = vertices_finais[int(idx) - 1]

                    if vertice1 != vertice2:  # Ignorando auto-conexões (A, A), (B, B) e etc
                        arestas.append([vertice1, vertice2])
                        print(f'  Vértice ligado = {vertice2} ({val})')
                    else:
                        print(f'  Vértice auto-conectado [({vertice1}, {vertice2}) ({val})] [* Ignorado *]')

        print('')
        print(f'Arestas: {arestas}')
        print('========')

        return arestas


def soma(a, b):
    return a + b
