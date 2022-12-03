from collections import defaultdict
import random


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)
        self.pesos = None
        self.rotulos = None

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

    def grafo_ciclico(self):
        """ Retorna True se o grafo for cíclico. """
        # Inicializa a pilha de busca.
        pilha = [self.get_vertices()[0]]
        # Inicializa a árvore de busca em profundidade.
        arvore = {pilha[0]: None}
        # Enquanto a pilha não estiver vazia.
        while pilha:
            # Retira o primeiro elemento da pilha.
            u = pilha.pop()
            # Para cada vértice adjacente a 'u'.
            for v in self.vertices_adjacentes(u):
                # Se o vértice ainda não foi visitado.
                if v not in arvore:
                    # Adiciona o vértice na árvore.
                    arvore[v] = u
                    # Adiciona o vértice na pilha.
                    pilha.append(v)
                # Se o vértice já foi visitado e não é o pai de 'u'.
                elif arvore[u] != v:
                    return True
        return False

    def caminho_minimo(self, s, t):
        """ Retorna o menor caminho entre os vértices 's' e 't'. """
        # Inicializa a árvore de busca em largura.
        arvore = self.busca_largura(s)
        # Se não existe caminho entre 's' e 't'.
        if t not in arvore:
            return None
        # Inicializa o caminho mínimo.
        caminho = [t]
        # Enquanto o vértice atual não for 's'.
        while caminho[-1] != s:
            # Adiciona o vértice pai no caminho mínimo.
            caminho.append(arvore[caminho[-1]])
        # Retorna o caminho mínimo.
        return caminho[::-1]

    def componentes_conexas(self):
        """ Retorna as componentes conexas do grafo. """
        # Inicializa a pilha de busca.
        pilha = []
        # Inicializa a lista de componentes conexas.
        componentes = []
        # Para cada vértice do grafo.
        for v in self.get_vertices():
            # Se o vértice ainda não foi visitado.
            if v not in pilha:
                # Inicializa a componente conexa.
                componente = []
                # Adiciona o vértice na pilha.
                pilha.append(v)
                # Enquanto a pilha não estiver vazia.
                while pilha:
                    # Retira o primeiro elemento da pilha.
                    u = pilha.pop()
                    # Adiciona o vértice na componente conexa.
                    componente.append(u)
                    # Para cada vértice adjacente a 'u'.
                    for w in self.vertices_adjacentes(u):
                        # Se o vértice ainda não foi visitado.
                        if w not in pilha:
                            # Adiciona o vértice na pilha.
                            pilha.append(w)
                # Adiciona a componente conexa na lista de componentes conexas.
                componentes.append(componente)
        # Retorna a lista de componentes conexas.
        return componentes

    def pondera_vertices(self, pesos):
        """ Pondera os vértices do grafo. """
        self.pesos = pesos

    def rotula_vertices(self, rotulos):
        """ Rotula os vértices do grafo. """
        self.rotulos = rotulos

    def rotula_arestas(self, rotulos):
        """ Rotula as arestas do grafo. """
        self.rotulos = rotulos

    def busca_largura(self, s):
        """ Retorna a árvore de busca em largura a partir do vértice 's'. """
        # Inicializa a árvore de busca em largura.
        arvore = {s: None}
        # Inicializa a fila de busca.
        fila = [s]
        # Enquanto a fila não estiver vazia.
        while fila:
            # Retira o primeiro elemento da fila.
            u = fila.pop(0)
            # Para cada vértice adjacente a 'u'.
            for v in self.vertices_adjacentes(u):
                # Se o vértice ainda não foi visitado.
                if v not in arvore:
                    # Adiciona o vértice na árvore.
                    arvore[v] = u
                    # Adiciona o vértice na fila.
                    fila.append(v)
        return arvore

    def busca_profundidade(self, s):
        """ Retorna a árvore de busca em profundidade a partir do vértice 's'. """
        # Inicializa a árvore de busca em profundidade.
        arvore = {s: None}
        # Inicializa a pilha de busca.
        pilha = [s]
        # Enquanto a pilha não estiver vazia.
        while pilha:
            # Retira o primeiro elemento da pilha.
            u = pilha.pop()
            # Para cada vértice adjacente a 'u'.
            for v in self.vertices_adjacentes(u):
                # Se o vértice ainda não foi visitado.
                if v not in arvore:
                    # Adiciona o vértice na árvore.
                    arvore[v] = u
                    # Adiciona o vértice na pilha.
                    pilha.append(v)
        return arvore

    def print_grafo(self):
        print(self.__str__())

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
