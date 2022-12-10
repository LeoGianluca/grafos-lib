class FileProcessor(object):
    """ Métodos utilitários para processamento de arquivos """

    # Tipos de arquivos possíveis para processamento
    FILE_TYPE_MATRIZ: str = 'matriz'
    FILE_TYPE_LISTA: str = 'lista'

    # Extensão dos arquivos possíveis para processamento
    FILE_TYPE_MATRIZ_EXT: str = '.adj_mtz'
    FILE_TYPE_LISTA_EXT: str = '.adj_list'
    FILE_TYPE_TXT_EXT: str = '.txt'

    # def __init__(self, data_input_dir: str = "./src/data/in", data_output_dir: str = "./src/data/out"):
    #     self.data_input_dir = data_input_dir
    #     self.data_output_dir = data_output_dir

    def read(self, file_path, file_type):
        print(f'Processando arquivo (arquivo={file_path}, tipo={file_type})')

        if file_type not in [self.FILE_TYPE_MATRIZ, self.FILE_TYPE_LISTA]:
            return print(f'Tipo de arquivo desconhecido [{file_type}]')

        file_content = self.read_file_matrix(file_path) \
            if file_type == self.FILE_TYPE_MATRIZ \
            else self.read_file_list(file_path)

        print('')
        print('Inspecionando dados obtidos do arquivo de entrada')
        print(file_content)
        print('')

        return file_content

    def read_file_list(self, file_path):
        """
        Realiza leitura de um arquivo de lista de adjacencias.

        :param file_path: caminho do arquivo a ser processado

        :return: representacao do conjunto de arestas do grafo
        """
        with open(file_path, 'r') as f:
            file_content = []

            for line in f.readlines():
                line = line.rstrip()  # Remove espacos a direita

                if line:  # Ignora o processamento em caso de linhas vazias
                    file_content.append([str(x) for x in line.split(';')])

        return file_content

    def read_file_matrix(self, file_path):
        """
        Realiza leitura de um arquivo de matriz de adjacencias.

        :param file_path: caminho do arquivo a ser processado

        :return: representacao do conjunto de arestas do grafo
        """
        with open(file_path, 'r') as f:
            arestas = []  # Lista de arestas do grafo
            vertices_finais = []  # Lista de vertices finais do grafo

            file_lines = [(line_num, line) for line_num, line in enumerate(f)]  # Lista de tuplas (numero da linha, conteudo da linha)

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
                        print(f'Processando conexões para o vértice {vertice1}')  # ignorando primeira valor (rótulo do vértice)
                        continue

                    peso_aresta = int(val)

                    if peso_aresta > 0:  # Verifica se peso da aresta > 0, se sim existe ligação entre os vértices
                        vertice2 = vertices_finais[int(idx) - 1]  # Atribui o valor do vertice final

                        if vertice1 != vertice2:  # Ignorando auto-conexões (A, A), (B, B) e etc
                            arestas.append([vertice1, vertice2, peso_aresta])  # Adiciona a aresta a lista de arestas
                            print(f'  Vértice ligado = {vertice2} (peso_aresta = {peso_aresta})')
                        else:  # Caso o vertice inicial seja igual ao vertice final
                            print(f'  Vértice auto-conectado [({vertice1}, {vertice2}) ({peso_aresta})] [* Ignorado *]')

            print('')
            print(f'Arestas: {arestas}')
            print('========')

            return arestas

    def write(self, file_path, file_type, file_content):
        print(f'Processando arquivo (arquivo={file_path}, tipo={file_type})')

        if file_type == self.FILE_TYPE_MATRIZ:  # Verifica se o tipo de arquivo é matriz
            self.write_file_graph_as_list(file_path, file_content)  # Chama a função write_file_matrix
        elif file_type == self.FILE_TYPE_LISTA:  # Verifica se o tipo de arquivo é lista
            self.write_file_graph_as_matrix(file_path, file_content)  # Chama a função write_file_list
        else:  # Caso o tipo de arquivo não seja nem matriz nem lista armazena o conteúdo do arquivo em um .txt
            self.write_file_plain_text(file_path, file_content)  # Chama a função write_file_plain_text

        print('')

    def write_file_plain_text(self, file_path, file_content):
        """
        Realiza escrita de um arquivo de texto.

        :param file_path: arquivo a ser processado
        :param file_content: conteudo a ser escrito no arquivo
        """
        with open(file_path, 'w') as f:
            f.write(file_content)

    def write_file_graph_as_list(self, file_path, file_content):
        """
        Realiza escrita de um arquivo de lista de adjacencias.

        :param file_path: arquivo a ser processado
        :param file_content: conteudo do arquivo a ser processado
        """
        with open(file_path, 'w') as f:
            for line in file_content:
                f.write(f'{line[0]};{line[1]}')

                if line != file_content[-1]:  # Verifica se é a ultima linha do arquivo
                    f.write('')  # Adiciona uma quebra de linha

    def write_file_graph_as_matrix(self, file_path, file_content):
        """
        Realiza escrita de um arquivo de matriz de adjacencias.

        :param file_path: arquivo a ser processado
        :param file_content: conteudo do arquivo a ser processado
        """

        def write_matrix_header(lines):
            for header_label in lines:
                header_vertex_0 = header_label[0]
                header_vertex_1 = header_label[1]
                
                if header_vertex_0 not in vertices:  # Verifica se o vertice inicial não está na lista de vertices
                    vertices.append(header_vertex_0)  # Adiciona o vertice inicial a lista de vertices
                if header_vertex_1 not in vertices:  # Verifica se o vertice final não está na lista de vertices
                    vertices.append(header_vertex_1)  # Adiciona o vertice final a lista de vertices

            file_header = f';{";".join(vertices)}'
            f.write(file_header + '\n')  # Escreve o cabecalho do arquivo

        with open(file_path, 'w') as f:
            vertices = []  # Lista de vertices do grafo

            write_matrix_header(file_content)

            for vertice1 in vertices:  # Itera sobre os vertices do grafo
                file_line = f'{vertice1}'  # Escreve o vertice inicial

                for vertice2 in vertices:  # Itera sobre os vertices do grafo
                    aresta_peso = 0  # Valor inicial do peso da aresta, por padrão considera os vértices desconectados

                    # Localiza o par de vértices e lê o valor do peso da aresta
                    for aresta in file_content:
                        if vertice1 == aresta[0] and vertice2 == aresta[1]:
                            aresta_peso = aresta[2]
                            break

                    file_line += f';{aresta_peso}'

                f.write(file_line + '\n')
