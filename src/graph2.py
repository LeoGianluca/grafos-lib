class Vertex(object):
    """ Classe que representa os vértices de um grafo """

    id_counter = 0

    def __init__(self, label, value, parent, children_vertex, children_edges):
        self.id = Vertex.id_counter
        Vertex.id_counter += 1

        self.label = label  # Rótulo do vérice (Ex: A. B, 35, 71a)
        self.value = value  # Valor do peso do vértice
        self.parent = parent  # Vértice pai deste vértice
        self.children_vertex = children_vertex
        self.children_edges = children_edges

    def add_edge(self, first, second, value):
        """ Adiciona uma aresta ao grafo. """

        e = Edge(first, second, value)
        print(e)

        self.vertex_list[first].children_vertex.append(second)
        self.vertex_list[first].children_edges.append(e)

        self.vertex_list[second].children_vertex.append(first)
        self.vertex_list[second].children_edges.append(e)

    def __repr__(self):
        return f"{type(self).__name__}({self.id}, {self.label}, {self.parent}, {self.children_vertex}, {self.children_edges})"


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
        self.root_vertex_list = None

        self.add_vertex(matriz_adj)  # Adiciona os vértices.

    def add_vertex(self, lista_adj):
        """ Retorna a lista de vértices do grafo. """

        for i in lista_adj:
            v1 = Vertex(i[0], 1, None, [], [])
            v2 = Vertex(i[1], 1, v1, [], [])

            e1 = Edge(v1, v2, i[2])

            v1.add_edge(e1)

            if self.v1.parent is None:
                print(f'Setando vertice raiz: {v1}')

                self.root_vertex_list.append(v1)

            GraphV2.vertex_counter += 1

    def __repr__(self):
        return f"{type(self).__name__}({self.root_vertex})"


if __name__ == '__main__':
    print('Teste grafo')

    # fileIn = 'data/in/teste-matriz-1.csv'
    # graph_info = file_processor.read(fileIn, 'matriz')
    graph_info = [['A', 'B', 4], ['A', 'C', 3], ['A', 'D', 2], ['A', 'E', 1]]

    grafo = GraphV2(graph_info)

    print()
    print(graph_info)
    print(grafo)
