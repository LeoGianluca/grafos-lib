from collections import deque


class Vertex(object):
    """ Classe que representa os vértices de um grafo """
    id_counter = 0

    def __init__(self, label: str, parent, children_edges=None):
        self.id = Vertex.id_counter
        self.label = label  # Rótulo do vérice (Ex: A. B, X, W, ...)
        self.parent = parent  # Vértice pai deste vértice

        if children_edges is None:
            self.children_edges = set()  # Lista de arestas originadas do vértice atual

        Vertex.id_counter += 1

    def add_edge(self, edge):
        """ Adiciona uma aresta ao grafo. """
        self.children_edges.add(edge)

    def remove_edge(self, edge):
        """ Remove uma aresta do grafo. """
        self.children_edges.remove(edge)

    def vertex_adjacency(self):
        """ Retorna os vértices adjacentes ao vértice atual. """
        return [edge.origin if edge.destination == self else edge.destination for edge in self.children_edges]

    def set_label_vertex(self, label):
        self.label = label

    def search_width(self, target):
        """ Busca em largura """
        visited = set()
        queue = deque()
        queue.append(self)

        while queue:
            vertex = queue.popleft()
            if vertex == target:
                return vertex
            visited.add(vertex)
            for edge in vertex.children_edges:
                if edge.origin == vertex:
                    if edge.destination not in visited:
                        queue.append(edge.destination)
                elif edge.destination == vertex:
                    if edge.origin not in visited:
                        queue.append(edge.origin)
        return None

    def search_depth(self, target):
        """ Busca em profundidade """
        visited = set()
        stack = list()
        stack.append(self)

        while stack:
            vertex = stack.pop()
            if vertex == target:
                return vertex
            visited.add(vertex)
            for edge in vertex.children_edges:
                if edge.origin == vertex:
                    if edge.destination not in visited:
                        stack.append(edge.destination)
                elif edge.destination == vertex:
                    if edge.origin not in visited:
                        stack.append(edge.origin)
        return None

    def is_eulerian(self):
        """ Verifica se o grafo é euleriano """
        for edge in self.children_edges:
            if edge.is_bridge():
                return False
        return True

    def algorithm_tarjan(self):
        """ Algoritmo de Tarjan """
        visited = set()
        stack = list()
        stack.append(self)

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
            for edge in vertex.children_edges:
                if edge.origin == vertex:
                    if edge.destination not in visited:
                        stack.append(edge.destination)
                elif edge.destination == vertex:
                    if edge.origin not in visited:
                        stack.append(edge.origin)
        return visited

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
        self.destination = first if self.first != self.second else None
        self.origin = second if self.first != self.second else None

        Vertex.id_counter += 1

    def is_bridge(self):
        """ Verifica se a aresta é uma ponte """
        if self.first == self.second:
            return False

        self.first.remove_edge(self)
        self.second.remove_edge(self)
        visited = self.first.algorithm_tarjan()
        self.first.add_edge(self)
        self.second.add_edge(self)
        return self.second not in visited

    def edge_adjacency(self):
        """ Retorna as arestas adjacentes à aresta atual. """
        return [edge for edge in self.first.children_edges if edge != self]

    def perform_edge_weighting(self, value):
        """ Insere o peso da aresta """
        self.value = value

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.first}, {self.second}, {self.value})\n"

    def __contains__(self, item):
        return item in (self.first, self.second)


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

    # busca em profundidade flag
    def remove_edge(self, edge):
        """ Remove uma aresta do grafo. """

        for vertex in self.root_vertex_list:
            if edge.first == vertex:
                vertex.remove_edge(edge)

    def search_width(self, vertex):
        """ Busca em largura. """

        for v in self.root_vertex_list:
            if v == vertex:
                return v.search_width(vertex)
        return None

    def search_depth(self, vertex):
        """ Busca em profundidade. """

        for v in self.root_vertex_list:
            if v == vertex:
                return v.search_depth(vertex)
        return None

    def tarjan(self):
        """ Algoritmo de Tarjan """
        visited = set()
        for vertex in self.root_vertex_list:
            visited.update(vertex.algorithm_tarjan())
        return visited

    def get_edges(self):
        """ Retorna as arestas do grafo. """
        edges = set()
        for vertex in self.root_vertex_list:
            edges.update(vertex.children_edges)
        return edges

    def get_vertex(self):
        """ Retorna os vértices do grafo. """
        return self.root_vertex_list

    def edge_contain(self, edge):
        """ Verifica se a aresta pertence ao grafo. """
        return edge in self.root_vertex_list.__contains__(edge)

    def edge_adjacency(self, edge):
        """ Verifica se a aresta é adjacente. """

        for vertex in self.root_vertex_list:
            if vertex == edge.first:
                return vertex.edge_adjacency(edge)
        return False

    def vertex_adjacency(self, vertex):
        """ Verifica se o vértice é adjacente. """

        for v in self.root_vertex_list:
            if v == vertex:
                return v.vertex_adjacency(vertex)
        return False

    def set_label_vertex(self):
        """ Define os rótulos dos vértices. """

        for vertex in self.root_vertex_list:
            vertex.set_label_vertex()

    def perform_edge_weighting(self):
        """ Realiza o peso das arestas. """

        for vertex in self.root_vertex_list:
            vertex.perform_edge_weighting()

    def __repr__(self):
        return f"{type(self).__name__}({self.root_vertex_list})"
