class Vertex(object):
    """ Classe que representa os vértices de um grafo """

    id_counter = 0

    def __init__(self, label, value, parent,  children_vertex, children_edges):
        self.id = Vertex.id_counter
        Vertex.id_counter += 1

        self.label = label  # Rótulo do vérice (Ex: A. B, 35, 71a)
        self.value = value  # Valor do peso do vértice
        self.parent = parent  # Vértice pai deste vértice
        self.children_vertex = children_vertex
        self.children_edges = children_edges

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.label}, {self.parent}, {self.children_vertex}, , {self.children_edges})"


class Edge(object):
    """ Classe que representa as arestas de um grafo """

    id_counter = 0

    def __init__(self, first, second, value):
        self.id = Vertex.id_counter
        Vertex.id_counter += 1

        self.first = first
        self.second = second
        self.value = value

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.first}, {self.second}, {self.value})"


class GraphV2(object):
    """ Implementação de um grafo. """

    vertex_counter = 0

    def __init__(self, matriz_adj):
        self.vertex_list = None

        self.add_vertex(matriz_adj)  # Adiciona os vértices.

    def add_vertex(self, matriz_adj):
        """ Retorna a lista de vértices do grafo. """

        for i in matriz_adj:
            v = Vertex(i, 10, None, [], [])
            print(v)

            if self.vertex_counter == 0:
                print("Setando vertice raiz: {v}")

                self.root_vertex = v

            GraphV2.vertex_counter += 1
    
    def __repr__(self):
        return f"{type(self).__name__}({self.root_vertex})"


if __name__ == '__main__':
    print('Teste grafo')

    grafo = GraphV2(['A', 'B', '15', '1a'])

    print()
    print(grafo)
