import random
from collections import defaultdict
from file_processor import FileProcessor

import graph


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    file_processor = FileProcessor()

    def __init__(self, input_format, input_content):
        self.input_format = input_format  # Formato de entrada
        self.input_content = input_content  # Conteúdo de entrada
        self.adj = defaultdict(set)  # Dicionário de adjacências

        # Se o conteúdo de entrada não for nulo
        if input_content is not None:
            # Cria um grafo com o conteúdo de entrada
            self.grafo = graph.Graph(input_content)
        # Se o conteúdo de entrada for nulo
        else:
            # O grafo é nulo
            self.grafo = None

    def criacao_grafo_x_vertices(self, extra_args, file_out_path):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        vertices = []  # Lista de vértices
        # Para cada vértice
        for i in range(0, int(extra_args)):
            # Gera um número aleatório entre 1 e 11000
            random_number = random.randint(1, 11000)
            # Se o número não estiver nos vértices
            if random_number not in vertices:
                # Adiciona o número aos vértices
                vertices.append(random_number)
            # Se o número estiver nos vértices
            else:
                # Gera um novo número aleatório entre 1 e 11000
                random_number = random.randint(1, 11000)
                # Adiciona o novo número aos vértices
                vertices.append(random_number)

        arestas = []  # Lista de arestas
        # Para cada vértice
        for i in range(1, len(vertices)):
            # Adiciona uma aresta entre o primeiro vértice e o vértice atual
            arestas.append((vertices[0], vertices[i], 1))

        # Cria um grafo com os vértices e as arestas
        graph.Graph(arestas)

        # Gravando arquivo de saída
        self.file_processor.write_file_graph_as_matrix(file_out_path, arestas)

    def criacao_arestas(self, extra_args, file_out_path):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        arestas = self.grafo.get_edges()

        # Lista de novas arestas
        novas_arestas = []
        # Para cada aresta
        for i in range(0, int(extra_args)):
            # Gera um número aleatório entre 1 e 11000
            random_number = random.randint(1, 11000)
            # Se o número não estiver nas arestas
            if random_number not in arestas:
                # Adiciona o número às novas arestas
                novas_arestas.append([i, random_number, 1])
            else:  # Se o número estiver nas arestas
                # Gera um novo número aleatório entre 1 e 11000
                random_number = random.randint(1, 11000)
                # Adiciona o novo número às novas arestas
                novas_arestas.append([i, random_number, 1])

        self.grafo.add_edge(novas_arestas)

    def remocao_arestas(self, extra_args, file_out_path):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")

        # Remove a aresta
        graph.Graph.remove_edge(self.grafo, extra_args)

    def rotulacao_vertices(self, extra_args, file_out_path):
        print(f"Execuntando 'rotulacao_vertices' [extra_args={extra_args}]")

        # Adiciona um rótulo ao vértice

        for vertex in self.grafo.root_vertex_list:
            vertex.set_label_vertex(extra_args)

    def ponderacao_vertices(self):
        print(f"Execuntando 'ponderacao_vertices'")

        # Adiciona um peso ao vértice
        self.grafo.perform_vertex_weighting()

    def ponderacao_arestas(self):
        print(f"Execuntando 'ponderacao_arestas'")

        # Adiciona um peso à aresta
        self.grafo.perform_edge_weighting()

    def rotulacao_arestas(self):
        print(f"Execuntando 'rotulacao_arestas'")

        # Adiciona um rótulo à aresta
        self.grafo.label_edge()

    def checagem_adjacencia_vertices(self, extra_args, file_out_path):
        print(f"Execuntando 'checagem_adjacencia_vertices' [extra_args={extra_args}]")

        # Checa se os vértices são adjacentes
        self.grafo.vertex_adjacency(extra_args)

    def checagem_adjacencia_arestas(self, extra_args, file_out_path):
        print(f"Execuntando 'checagem_adjacencia_arestas' [extra_args={extra_args}]")

        # Checa se as arestas são adjacentes
        self.grafo.edge_adjacency(extra_args)

    def checagem_existencia_arestas(self, extra_args, file_out_path):
        print(f"Execuntando 'checagem_existencia_arestas' [extra_args={extra_args}]")

        # Verifica se a aresta existe
        if self.grafo.has_edge(extra_args):
            print(f"Aresta {extra_args} existe")
        else:
            print(f"Aresta {extra_args} não existe")

    def checagem_quantidade_vertices(self):
        print(f"Execuntando 'checagem_quantidade_vertices'")

        # Retorna a quantidade de vértices
        print(f"Quantidade de vértices: {self.grafo.get_number_vertices()}")

    def checagem_quantidade_arestas(self):  # Imprime a quantidade de arestas
        print(f"Execuntando 'checagem_quantidade_arestas'")

        print(f"Quantidade de arestas: {self.grafo.get_number_edges()}")

    def checagem_grafo_vazio(self):
        print(f"Execuntando 'checagem_grafo_vazio'")

        # Verifica se o grafo está vazio
        if self.grafo.is_empty():
            print("Grafo vazio")
        else:
            print("Grafo não vazio")

    def checagem_grafo_completo(self):
        print(f"Execuntando 'checagem_grafo_completo'")

        # Verifica se o grafo é completo
        if self.grafo.is_complete():
            print("Grafo completo")
        else:
            print("Grafo não completo")

    def naive(self, extra_args):
        print(f"Execuntando 'naive' [extra_args={extra_args}]")

        # Executa o algoritmo naive utilizando busca em profundidade
        self.grafo.search_depth(extra_args)

    def algorithm_fluery(self, extra_args):
        print(f"Execuntando 'fleury' [extra_args={extra_args}]")

        # Verifica se o grafo é euleriano
        if not self.grafo.is_eulerian():  # Se não for euleriano
            print("Grafo não é euleriano")
        else:  # Se for euleriano
            self.grafo.algorithm_fleury(extra_args)

    def algorithm_tarjan(self):
        print(f"Execuntando 'tarjan'")

        # Executa o algoritmo de Tarjan
        self.grafo.tarjan()
