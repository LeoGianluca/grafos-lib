"""
Métodos utilitários para processamento de arquivos
"""


def read(file, file_type):
    print(f'Processando arquivo (arquivo={file}, tipo={file_type})')

    if file_type == 'matriz':  # Verifica se o tipo de arquivo é matriz
        file_content = read_file_matrix(file)  # Chama a função read_file_matrix
    elif file_type == 'lista':  # Verifica se o tipo de arquivo é lista
        file_content = read_file_list(file)  # Chama a função read_file_list
    else:  # Caso o tipo de arquivo não seja nem matriz nem lista
        return print(f'Tipo de arquivo desconhecido [{file_type}]')  # Imprime a mensagem de erro

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
        arestas = []  # Lista de arestas do grafo
        vertices_finais = []  # Lista de vertices finais do grafo

        file_lines = [(line_num, line) for line_num, line in
                      enumerate(f)]  # Lista de tuplas (numero da linha, conteudo da linha)

        print('')

        for line in file_lines:  # Itera sobre as linhas do arquivo
            line_number = line[0]  # Numero da linha
            line_content = line[1]  # Conteudo da linha

            line_splited_values = line_content.rstrip().split(';')  # Separa os valores da linha

            # Processando primeira linha do arquivo,
            # referente ao cabecalho com lista de nós em colunas
            if line_number == 0:  # Verifica se é a primeira linha do arquivo
                vertices_finais = line_splited_values  # Atribui a lista de vertices finais
                vertices_finais.pop(0)  # Remove o primeiro elemento da lista, que é o cabecalho
                continue

            line_values = list()  # Lista de valores da linha

            for val in line_splited_values:  # Itera sobre os valores da linha
                line_values.append(val)  # Adiciona o valor a lista de valores da linha

            for idx, val in enumerate(line_values):  # Itera sobre os valores da linha
                if idx == 0:  # Verifica se é o primeiro valor da linha
                    vertice1 = line_values[0]  # Atribui o valor do vertice inicial
                    print(
                        f'Processando conexões para o vértice {vertice1}')  # ignorando primeira valor (rótulo do vértice)
                    continue

                if int(val) > 0:  # Verifica se o valor é maior que zero
                    vertice2 = vertices_finais[int(idx) - 1]  # Atribui o valor do vertice final

                    if vertice1 != vertice2:  # Ignorando auto-conexões (A, A), (B, B) e etc
                        arestas.append([vertice1, vertice2])  # Adiciona a aresta a lista de arestas
                        print(f'  Vértice ligado = {vertice2} ({val})')
                    else:  # Caso o vertice inicial seja igual ao vertice final
                        print(f'  Vértice auto-conectado [({vertice1}, {vertice2}) ({val})] [* Ignorado *]')

        print('')
        print(f'Arestas: {arestas}')
        print('========')

        return arestas


def write(file, file_type, file_content):
    print(f'Processando arquivo (arquivo={file}, tipo={file_type})')

    if file_type == 'matriz':  # Verifica se o tipo de arquivo é matriz
        write_file_matrix(file, file_content)  # Chama a função write_file_matrix
    elif file_type == 'lista':  # Verifica se o tipo de arquivo é lista
        write_file_list(file, file_content)  # Chama a função write_file_list
    else:  # Caso o tipo de arquivo não seja nem matriz nem lista
        print(f'Tipo de arquivo desconhecido [{file_type}]')  # Imprime a mensagem de erro

    print('')


def write_file_list(file, file_content):
    """
    Realiza escrita de um arquivo de lista de adjacencias.

    :param file: arquivo a ser processado
    :param file_content: conteudo do arquivo a ser processado
    """
    with open(file, 'w') as f:
        for line in file_content:
            f.write(f'{line[0]};{line[1]}')

            if line != file_content[-1]:  # Verifica se é a ultima linha do arquivo
                f.write('')  # Adiciona uma quebra de linha


def write_file_matrix(file, file_content):
    """
    Realiza escrita de um arquivo de matriz de adjacencias.

    :param file: arquivo a ser processado
    :param file_content: conteudo do arquivo a ser processado
    """
    with open(file, 'w') as f:
        vertices = []  # Lista de vertices do grafo

        for aresta in file_content:  # Itera sobre as arestas do grafo
            if aresta[0] not in vertices:  # Verifica se o vertice inicial não está na lista de vertices
                vertices.append(aresta[0])  # Adiciona o vertice inicial a lista de vertices

            if aresta[1] not in vertices:  # Verifica se o vertice final não está na lista de vertices
                vertices.append(aresta[1])  # Adiciona o vertice final a lista de vertices

        f.write(f';{";".join(vertices)}')  # Escreve o cabecalho do arquivo

        for vertice1 in vertices:  # Itera sobre os vertices do grafo
            f.write(f'{vertice1}')  # Escreve o vertice inicial

            for vertice2 in vertices:  # Itera sobre os vertices do grafo
                if vertice1 == vertice2:  # Verifica se o vertice inicial é igual ao vertice final
                    f.write(';0')  # Escreve o valor zero
                else:  # Caso o vertice inicial seja diferente do vertice final
                    if [vertice1, vertice2] in file_content:  # Verifica se a aresta existe no grafo
                        f.write(';1')  # Escreve o valor um
                    else:  # Caso a aresta não exista no grafo
                        f.write(';0')  # Escreve o valor zero

            if vertice1 != vertices[-1]:  # Verifica se é a ultima linha do arquivo
                f.write('')  # Adiciona uma quebra de linha
