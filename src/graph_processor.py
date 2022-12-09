import random
from collections import defaultdict

import graph
import graph2


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content):
        self.input_format = input_format  # Formato de entrada
        self.input_content = input_content  # Conteúdo de entrada
        self.adj = defaultdict(set)  # Dicionário de adjacências

        if input_content is not None:  # Se o conteúdo de entrada não for nulo
            self.grafo = graph.Grafo(input_content)  # Cria um grafo com o conteúdo de entrada
        else:  # Se o conteúdo de entrada for nulo
            self.grafo = None  # O grafo é nulo

        if input_content is not None:  # Se o conteúdo de entrada não for nulo
            self.grafoV2 = graph2.GraphV2(input_content)  # Cria um grafo com o conteúdo de entrada
        else:  # Se o conteúdo de entrada for nulo
            self.grafoV2 = None  # O grafo é nulo

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        # Gerando um grafo com x vértices aleatóriamente com letras de A a Z não repetidas
        vertices = []  # Lista de vértices
        for i in range(0, int(extra_args)):  # Para cada vértice
            random_number = random.randint(1, 11000)  # Gera um número aleatório entre 1 e 11000
            if random_number not in vertices:  # Se o número não estiver nos vértices
                vertices.append(random_number)  # Adiciona o número aos vértices
            else:  # Se o número estiver nos vértices
                random_number = random.randint(1, 11000)  # Gera um novo número aleatório entre 1 e 11000
                vertices.append(random_number)  # Adiciona o novo número aos vértices

        # Víncula os vertices ao primeiro vertice
        arestas = []  # Lista de arestas
        for i in range(1, len(vertices)):  # Para cada vértice
            arestas.append((vertices[0], vertices[i]))  # Adiciona uma aresta entre o primeiro vértice e o vértice atual

        # Cria e imprime o grafo. O grafo é criado com os vértices e as arestas
        self.grafo = graph.Grafo(vertices, arestas, direcionado=True)  # Cria um grafo com as arestas e direcionado
        return self.grafo  # Retorna o grafo

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        arestas = self.grafo.get_arestas()  # Pega as arestas do grafo
        novas_arestas = []  # Lista de novas arestas
        for i in range(0, int(extra_args)):  # Para cada aresta
            random_number = random.randint(1, 11000)  # Gera um número aleatório entre 1 e 11000
            if random_number not in arestas:  # Se o número não estiver nas arestas
                novas_arestas.append([i, random_number])  # Adiciona o número às novas arestas
            else:  # Se o número estiver nas arestas
                random_number = random.randint(1, 11000)  # Gera um novo número aleatório entre 1 e 11000
                novas_arestas.append([i, random_number])  # Adiciona o novo número às novas arestas

        self.grafo.adiciona_arestas(novas_arestas)  # Adiciona as novas arestas ao grafo

    def remocao_arestas(self, extra_args):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")

        graph2.GraphV2.remove_edge(self.grafoV2, extra_args)

    def rotulacao_vertices(self, extra_args):
        print(f"Execuntando 'rotulacao_vertices' [extra_args={extra_args}]")
        # TODO: Implementar rotulacao_vertices (ERROR)
        # cria um dicionário com os vértices e seus rótulos
        self.grafo.rotulos = extra_args
        print(self.grafo.get_rotulo())

    def ponderacao_vertices(self):
        print(f"Execuntando 'ponderacao_vertices'")
        self.grafo.pondera_vertices()
        # TODO: Implementar ponderacao_vertices
        pass

    def ponderacao_arestas(self, extra_args):
        print(f"Execuntando 'ponderacao_arestas' [extra_args={extra_args}]")
        self.grafo.pondera_arestas(extra_args)  # Pondera as arestas

    def rotulacao_arestas(self, extra_args):
        print(f"Execuntando 'rotulacao_arestas' [extra_args={extra_args}]")
        self.grafoV2.label_edge(extra_args)

    def checagem_adjacencia_vertices(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_vertices' [extra_args={extra_args}]")

        self.grafoV2.vertex_adjacency(extra_args)

    def checagem_adjacencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_arestas' [extra_args={extra_args}]")

        self.grafoV2.edge_adjacency(extra_args)

    def checagem_existencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_existencia_arestas' [extra_args={extra_args}]")

        # Verifica se a aresta existe
        if self.grafoV2.has_edge(extra_args):
            print(f"Aresta {extra_args} existe")

    def checagem_quantidade_vertices(self):
        print(f"Execuntando 'checagem_quantidade_vertices'")

        print(f"Quantidade de vertices: {len(self.grafo.get_vertex())}")  # Imprime a quantidade de vértices

    def checagem_quantidade_arestas(self):  # Imprime a quantidade de arestas
        print(f"Execuntando 'checagem_quantidade_arestas'")

        print(f"Quantidade de arestas: {len(self.grafoV2.get_edges())}")  # Imprime a quantidade de arestas

    def checagem_grafo_vazio(self):
        print(f"Execuntando 'checagem_grafo_vazio'")

        for vertex in self.grafoV2.root_vertex_list:  # Para cada vértice
            if vertex.get_edge_list():
                print("Grafo não vazio")
                return
        print("Grafo vazio")

    def checagem_grafo_completo(self):
        print(f"Execuntando 'checagem_grafo_completo'")

        for vertex in self.grafoV2.root_vertex_list:
            if len(vertex.edges) != len(self.grafoV2.root_vertex_list) - 1:
                return False
        return True

    def naive(self, extra_args):
        print(f"Execuntando 'naive' [extra_args={extra_args}]")
        self.grafoV2.search_depth(extra_args)

    def fleury(self, extra_args):
        print(f"Execuntando 'fleury' [extra_args={extra_args}]")
        if not self.grafoV2.is_eulerian():
            return None
        else:
            self.grafoV2.fleury(extra_args)

    def algorithm_tarjan(self):
        print(f"Execuntando 'tarjan'")
        self.grafoV2.tarjan()
