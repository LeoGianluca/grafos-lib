class Vertex(object):
    """ Classe que representa os vértices de um grafo """
    id_counter = 0

    # def __init__(self, label: str, value: int, parent, children_edges=None):
    def __init__(self, label: str, parent, children_edges=None):
        self.id = Vertex.id_counter
        self.label = label  # Rótulo do vérice (Ex: A. B, X, W, ...)
        self.parent = parent  # Vértice pai deste vértice
        # self.value = value  # Valor do peso do vértice (Ex: 3, 5, 17, 21, ...)

        if children_edges is None:
            self.children_edges = set()  # Lista de arestas originadas do vértice atual

        Vertex.id_counter += 1

    def add_edge(self, edge):
        """ Adiciona uma aresta ao grafo. """
        self.children_edges.add(edge)

    def __eq__(self, other):
        return self.label == other.label if isinstance(other, type(self)) else False

    def __hash__(self):
        return hash((self.label, self.parent))

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.label}, {self.parent})"


class Edge(object):
    """ Classe que representa as arestas de um grafo """
    id_counter = 0

    def __init__(self, first, second, value):
        self.id = Vertex.id_counter
        self.first = first
        self.second = second
        self.value = value

        Vertex.id_counter += 1

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.first}, {self.second}, {self.value})\n"


class GraphV2(object):
    """ Implementação de um grafo. """
    vertex_counter = 0

    def __init__(self, matriz_adj):
        self.root_vertex_list = set()

        self.add_vertex(matriz_adj)  # Adiciona os vértices.

    def add_vertex(self, lista_adj):
        """ Retorna a lista de vértices do grafo. """
        v1 = None

        for idx, value in enumerate(lista_adj):
            if idx == 0:
                v1 = Vertex(value[0], None, None)

            v2 = Vertex(value[1], v1, None)

            e1 = Edge(v1, v2, value[2])

            v1.add_edge(e1)

            # Setando vertice raiz
            if GraphV2.vertex_counter == 0 or v1.parent is None:
                self.root_vertex_list.add(v1)

            GraphV2.vertex_counter += 1

    def __repr__(self):
        return f"{type(self).__name__}({self.root_vertex_list})"
