from collections import defaultdict
import random

from graph import Grafo


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content):
        self.input_format = input_format
        self.input_content = input_content
        self.adj = defaultdict(set)
        if input_content is not None:
            self.grafo = Grafo(input_content)
        else:
            self.grafo = None

        print(f'Arestas: {self.grafo.get_arestas()}')

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        # Gerando um grafo com x vértices aleatóriamente com letras de A a Z não repetidas
        vertices = []
        for i in range(0, int(extra_args)):
            randomNumber = random.randint(1, 1000)
            if randomNumber not in vertices:
                vertices.append(randomNumber)
            else:
                randomNumber = random.randint(1, 1000)
                vertices.append(randomNumber)

        print("Vertices: ", vertices)

        # Víncula os vertices ao primeiro vertice
        arestas = []
        for i in range(1, len(vertices)):
            arestas.append((vertices[0], vertices[i]))

        # Cria e imprime o grafo.
        self.grafo = Grafo(arestas, direcionado=True)
        print(self.grafo.adj)

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        for i in range(0, int(extra_args)):
            randomUpperLetter = self.grafo.vertices 

    def remocao_arestas(self, extra_args):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")
        print(self.input_content)
        pass

    def ponderacao_vertices(self):
        print(f"Execuntando 'ponderacao_vertices'")
        print(self.input_content)
        pass

    def rotulacao_vertices(self):
        print(f"Execuntando 'rotulacao_vertices'")
        print(self.input_content)
        pass

    def ponderacao_arestas(self):
        print(f"Execuntando 'ponderacao_arestas'")
        print(self.input_content)
        pass

    def rotulacao_arestas(self):
        print(f"Execuntando 'rotulacao_arestas'")
        print(self.input_content)
        pass

    def checagem_adjacencia_vertices(self):
        print(f"Execuntando 'checagem_adjacencia_vertices'")
        print(self.input_content)
        pass

    def checagem_adjacencia_arestas(self):
        print(f"Execuntando 'checagem_adjacencia_arestas'")
        print(self.input_content)
        pass

    def checagem_existencia_arestas(self):
        print(f"Execuntando 'checagem_existencia_arestas'")
        print(self.input_content)
        pass

    def checagem_quantidade_vertices(self):
        print(f"Execuntando 'checagem_quantidade_vertices'")
        print(self.input_content)
        pass

    def checagem_quantidade_arestas(self):
        print(f"Execuntando 'checagem_quantidade_arestas'")
        print(self.input_content)
        pass

    def checagem_grafo_vazio(self):
        print(f"Execuntando 'checagem_grafo_vazio'")
        print(self.input_content)
        pass

    def checagem_grafo_completo(self):
        print(f"Execuntando 'checagem_grafo_completo'")
        print(self.input_content)
        pass
