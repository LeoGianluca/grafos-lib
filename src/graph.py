from collections import defaultdict
import random


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        if u in self.adj:
            v in self.adj[u]
        else:
            return False

    def remove_arco(self, u, v):
        """ Remove a ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].remove(v)
        # Se o grafo é não-direcionado, precisamos remover arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].remove(u)

    def vertices_adjacentes(self, v):
        """ Retorna os vértices adjacentes ao vértice 'v'. """
        return self.adj[v]

    def arestas_adjacentes(self, v):
        """ Retorna as arestas adjacentes ao vértice 'v'. """
        return [(v, u) for u in self.adj[v]]

    def grafo_completo(self):
        """ Retorna um grafo completo. """
        arestas = [(i, j) for i in self.get_vertices() for j in self.get_vertices()]
        return Grafo(arestas, self.direcionado)

    def print_grafo(self):
        print(self.__str__())

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
