from collections import defaultdict

from graph import Grafo


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content, directed=False):
        self.input_format = input_format
        self.input_content = input_content
        self.adj = defaultdict(set)
        self.directed = directed

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        for i in range(0, int(extra_args)):
            randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
            self.adj[randomUpperLetter] = set()

        # Cria a lista de arestas.
        arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

        # Cria e imprime o grafo.
        grafo = Grafo(arestas, direcionado=True)
        print(grafo.adj)

        # graph = graphlib(self.adj, self.directed)

        # graph.print()

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

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
