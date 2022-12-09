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
        """ Define o rótulo do vértice """
        self.label = label

    def search_width(self, target):
        """ Busca em largura """
        visited = set()  # Conjunto de vértices visitados
        queue = deque()  # Fila de vértices
        queue.append(self)  # Adiciona o vértice atual na fila

        # Enquanto a fila não estiver vazia
        while queue:
            # Retira o primeiro elemento da fila
            vertex = queue.popleft()
            # Se o vértice for o alvo
            if vertex == target:
                # Retorna o vértice
                return vertex
            # Adiciona o vértice na lista de visitados
            visited.add(vertex)
            # Para cada aresta do vértice
            for edge in vertex.children_edges:
                # Se o vértice for o vértice de origem da aresta
                if edge.origin == vertex:
                    # Se o vértice de destino da aresta não estiver na lista de visitados
                    if edge.destination not in visited:
                        # Adiciona o vértice de destino na fila
                        queue.append(edge.destination)
                # Se o vértice for o vértice de destino da aresta
                elif edge.destination == vertex:
                    # Se o vértice de origem da aresta não estiver na lista de visitados
                    if edge.origin not in visited:
                        # Adiciona o vértice de origem na fila
                        queue.append(edge.origin)
        return None

    def search_depth(self, target):
        """ Busca em profundidade """
        visited = set()  # Conjunto de vértices visitados
        stack = list()  # Pilha de vértices
        stack.append(self)  # Adiciona o vértice atual na pilha

        # Enquanto a pilha não estiver vazia
        while stack:
            # Retira o último elemento da pilha
            vertex = stack.pop()
            # Se o vértice for o alvo
            if vertex == target:
                # Retorna o vértice
                return vertex
            # Adiciona o vértice na lista de visitados
            visited.add(vertex)
            # Para cada aresta do vértice
            for edge in vertex.children_edges:
                # Se o vértice for o vértice de origem da aresta
                if edge.origin == vertex:
                    # Se o vértice de destino da aresta não estiver na lista de visitados
                    if edge.destination not in visited:
                        # Adiciona o vértice de destino na pilha
                        stack.append(edge.destination)
                # Se o vértice for o vértice de destino da aresta
                elif edge.destination == vertex:
                    # Se o vértice de origem da aresta não estiver na lista de visitados
                    if edge.origin not in visited:
                        # Adiciona o vértice de origem na pilha
                        stack.append(edge.origin)
        return None

    def is_eulerian(self):
        """ Verifica se o grafo é euleriano """

        # Se o grafo for conexo
        for edge in self.children_edges:
            if edge.is_bridge():
                return False

        return True

    def algorithm_tarjan(self):
        """ Algoritmo de Tarjan """
        visited = set()  # Conjunto de vértices visitados
        stack = list()  # Pilha de vértices
        stack.append(self)  # Adiciona o vértice atual na pilha

        # Enquanto a pilha não estiver vazia
        while stack:
            # Retira o último elemento da pilha
            vertex = stack.pop()
            # Se o vértice for o alvo
            if vertex not in visited:
                # Retorna o vértice
                visited.add(vertex)
            # Adiciona o vértice na lista de visitados
            for edge in vertex.children_edges:
                # Se o vértice for o vértice de origem da aresta
                if edge.origin == vertex:
                    # Se o vértice de destino da aresta não estiver na lista de visitados
                    if edge.destination not in visited:
                        # Adiciona o vértice de destino na pilha
                        stack.append(edge.destination)
                # Se o vértice for o vértice de destino da aresta
                elif edge.destination == vertex:
                    # Se o vértice de origem da aresta não estiver na lista de visitados
                    if edge.origin not in visited:
                        # Adiciona o vértice de origem na pilha
                        stack.append(edge.origin)
        return visited

    def vertex_weighting(self):
        """ Retorna o peso do vértice """

        # Se o vértice for o vértice de origem da aresta
        return sum(edge.weight for edge in self.children_edges)

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

        # Se o vértice de origem da aresta for o vértice de destino da aresta
        if self.first == self.second:
            return False

        self.first.remove_edge(self)  # Remove a aresta do vértice de origem
        self.second.remove_edge(self)  # Remove a aresta do vértice de destino
        visited = self.first.algorithm_tarjan()  # Executa o algoritmo de Tarjan
        self.first.add_edge(self)  # Adiciona a aresta no vértice de origem
        self.second.add_edge(self)  # Adiciona a aresta no vértice de destino
        return self.second not in visited  # Retorna se o vértice de destino está na lista de visitados

    def edge_adjacency(self):
        """ Retorna as arestas adjacentes à aresta atual. """

        # Retorna as arestas adjacentes à aresta atual
        return [edge for edge in self.first.children_edges if edge != self]

    def edge_weighting(self, value):
        """ Retorna o peso da aresta """
        return self.value + value  # Retorna o peso da aresta

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.first}, {self.second}, {self.value})\n"

    def __contains__(self, item):
        return item in (self.first, self.second)


class Graph(object):
    """ Implementação de um grafo. """
    vertex_counter = 0

    def __init__(self, matriz_adj):
        self.root_vertex_list = set()  # Lista de vértices raiz

        self.add_vertex(matriz_adj)  # Adiciona os vértices.

    def add_vertex(self, lista_adj):
        """ Retorna a lista de vértices do grafo. """
        v1 = None  # Vértice 1

        # Para cada linha da matriz de adjacência
        for idx, value in enumerate(lista_adj):
            # Se o vértice 1 for None
            if idx == 0:  # Se for a primeira linha
                v1 = Vertex(value[0], None, None)  # Cria o vértice 1

            v2 = Vertex(value[1], v1, None)  # Cria o vértice 2

            e1 = Edge(v1, v2, value[2])  # Cria a aresta 1

            v1.add_edge(e1)  # Adiciona a aresta 1 no vértice 1

            # Se o vértice 2 não estiver na lista de vértices raiz
            if Graph.vertex_counter == 0 or v1.parent is None:
                # Adiciona o vértice 2 na lista de vértices raiz
                self.root_vertex_list.add(v1)

            # Se o vértice 1 não estiver na lista de vértices raiz
            Graph.vertex_counter += 1

    def add_edge(self, first, second, value):
        """ Adiciona uma aresta ao grafo. """

        # Se o vértice 1 for o vértice 2
        if first == second:
            raise ValueError("Não é possível criar uma aresta entre um vértice e ele mesmo.")

        self.add_vertex()  # Adiciona os vértices
        self.add_vertex()  # Adiciona os vértices

        e1 = Edge(first, second, value)  # Cria a aresta 1

        first.add_edge(e1)  # Adiciona a aresta 1 no vértice 1
        second.add_edge(e1)  # Adiciona a aresta 1 no vértice 2

    def remove_edge(self, edge):
        """ Remove uma aresta do grafo. """

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            if edge.first == vertex:  # Se o vértice 1 for o vértice 1 da aresta
                vertex.remove_edge(edge)  # Remove a aresta do vértice 1

    def search_width(self, vertex):
        """ Busca em largura. """

        for v in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            if v == vertex:  # Se o vértice for o vértice de origem
                return v.search_width(vertex)  # Retorna a busca em largura
        return None

    def search_depth(self, vertex):
        """ Busca em profundidade. """

        for v in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            if v == vertex:  # Se o vértice for o vértice de origem
                return v.search_depth(vertex)  # Retorna a busca em profundidade
        return None

    def tarjan(self):
        """ Algoritmo de Tarjan """

        visited = set()  # Lista de vértices visitados

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            visited.update(vertex.algorithm_tarjan())  # Atualiza a lista de vértices visitados

        return visited  # Retorna a lista de vértices visitados

    def get_edges(self):
        """ Retorna as arestas do grafo. """

        edges = set()  # Lista de arestas

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            edges.update(vertex.children_edges)  # Atualiza a lista de arestas

        return edges  # Retorna a lista de arestas

    def edge_contain(self, edge):
        """ Verifica se a aresta pertence ao grafo. """
        return edge in self.root_vertex_list.__contains__(edge)  # Retorna se a aresta pertence ao grafo

    def edge_adjacency(self, edge):
        """ Verifica se a aresta é adjacente. """

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            if vertex == edge.first:  # Se o vértice for o vértice 1 da aresta
                return vertex.edge_adjacency(edge)  # Retorna as arestas adjacentes à aresta

        return False  # Retorna False

    def vertex_adjacency(self, vertex):
        """ Verifica se o vértice é adjacente. """

        for v in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            if v == vertex:  # Se o vértice for o vértice de origem
                return v.vertex_adjacency(vertex)  # Retorna os vértices adjacentes ao vértice

        return False

    def set_label_vertex(self):
        """ Define os rótulos dos vértices. """

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            vertex.set_label_vertex()  # Define o rótulo do vértice

    def perform_edge_weighting(self):
        """ Realiza o peso das arestas. """

        for edge in self.get_edges():  # Para cada aresta na lista de arestas
            if not edge.is_bridge():  # Se a aresta não for uma ponte
                edge.edge_weighting(0)  # Realiza o peso da aresta
            else:  # Se a aresta for uma ponte
                edge.edge_weighting(1)  # Realiza o peso da aresta

    def perform_vertex_weighting(self):
        """ Realiza o peso dos vértices. """

        for vertex in self.root_vertex_list:  # Para cada vértice na lista de vértices raiz
            vertex.vertex_weighting()  # Realiza o peso do vértice

    def get_number_vertices(self):
        """ Retorna o número de vértices do grafo. """
        return len(self.root_vertex_list)  # Retorna o número de vértices do grafo

    def get_number_edges(self):
        """ Retorna o número de arestas do grafo. """
        return len(self.get_edges())  # Retorna o número de arestas do grafo

    def has_edge(self, edge):
        """ Verifica se o grafo possui a aresta. """
        return edge in self.get_edges()

    def is_empty(self):
        """ Verifica se o grafo está vazio. """
        return self.root_vertex_list == set()  # Retorna se o grafo está vazio

    def is_complete(self):
        """ Verifica se o grafo é completo. """
        # Retorna se o grafo é completo
        return self.get_number_edges() == (self.get_number_vertices() * (self.get_number_vertices() - 1)) / 2

    def __repr__(self):
        return f"{type(self).__name__}({self.root_vertex_list})"
