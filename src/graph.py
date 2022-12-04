from collections import defaultdict
import random


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, vertices, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)  # Dicionário de adjacências.
        self.direcionado = direcionado  # O grafo é direcionado?
        self.adiciona_vertices(vertices)  # Adiciona os vértices.
        self.adiciona_arestas(arestas)  # Adiciona as arestas ao grafo.
        self.pesos = None  # Peso dos vértices.
        self.rotulos = {}  # Rótulos dos vértices.

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        # Retorna a lista de vértices.
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        # Retorna a lista de arestas.
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def get_rotulo(self):
        """ Retorna o rótulo do vértice 'v'. """
        # Retorna o rótulo do vértice.
        return self.rotulos

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        # Para cada aresta.
        # Se o grafo for direcionado, adiciona apenas a aresta (u, v).
        # Se o grafo for não-direcionado, adiciona as arestas (u, v) e (v, u).
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_vertices(self, vertices):
        """ Adiciona vértices ao grafo. """
        # Para cada vértice.
        for v in vertices:
            # Adiciona o vértice ao grafo.
            self.adj[v]

    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        # Retorna True se 'u' e 'v' são adjacentes.
        if u in self.adj:
            v in self.adj[u]
        else:
            return False

    def remove_arco(self, u, v):
        """ Remove a ligação (arco) entre os nodos 'u' e 'v'. """
        # Remove a ligação (arco) entre os nodos 'u' e 'v'.
        self.adj[u].remove(v)
        # Se o grafo é não-direcionado, precisamos remover arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].remove(u)

    def vertices_adjacentes(self, v):
        """ Retorna os vértices adjacentes ao vértice 'v'. """
        # Retorna os vértices adjacentes.
        return self.adj[v]

    def arestas_adjacentes(self, v):
        """ Retorna as arestas adjacentes ao vértice 'v'. """
        # Retorna as arestas adjacentes.
        return [(v, u) for u in self.adj[v]]

    def grafo_completo(self):
        """ Retorna um grafo completo. """
        # Inicializa o grafo completo.
        arestas = [(i, j) for i in self.get_vertices() for j in self.get_vertices()]
        # Retorna o grafo completo.
        if self.direcionado:
            return Grafo(self.get_vertices(), arestas, direcionado=True)
        else:
            return Grafo(self.get_vertices(), arestas)

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

    def pondera_vertices(self, pesos):
        """ Pondera os vértices do grafo. """
        # Inicializa o dicionário de pesos.
        self.pesos = {}
        # Para cada vértice do grafo.
        for v in self.get_vertices():
            # Adiciona o peso do vértice.
            self.pesos[v] = pesos[v]

    def set_rotulos(self, rotulos):
        """ Define os rótulos dos vértices do grafo. """
        # recebe os vertices
        vertices = self.get_vertices()
        # cria um dicionario de rotulos
        self.rotulos = {}
        # para cada vertice
        for i in range(len(vertices)):
            # adiciona o rotulo
            self.rotulos[vertices[i]] = rotulos[i]

    def rotula_arestas(self, rotulos):
        """ Rotula as arestas do grafo. """
        # Inicializa o dicionário de rótulos.
        self.rotulos = {}
        # Para cada aresta do grafo.
        for a in self.get_arestas():
            # Adiciona o rótulo da aresta.
            self.rotulos[a] = rotulos[a]

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

    def naive_profundidade(self, s):
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

    def fleury(self, s):
        """ Retorna um ciclo euleriano a partir do vértice 's'. """
        # Inicializa o ciclo euleriano.
        ciclo = [s]
        # Enquanto o grafo não estiver vazio.
        while self.get_vertices():
            # Para cada vértice adjacente ao vértice atual.
            for v in self.vertices_adjacentes(ciclo[-1]):
                # Se a aresta não é ponte.
                if not self.is_ponte(ciclo[-1], v):
                    # Adiciona o vértice adjacente ao ciclo euleriano.
                    ciclo.append(v)
                    # Remove a aresta do grafo.
                    self.remove_arco(self, ciclo[-2], ciclo[-1])
                    # Para o laço.
                    break
        # Retorna o ciclo euleriano.
        return ciclo

    def is_ponte(self, u, v):
        """ Retorna True se a aresta (u, v) é ponte. """
        # Remove a aresta do grafo.
        self.remove_arco(u, v)
        # Se a aresta é ponte.
        if not self.eh_conexo():
            # Adiciona a aresta no grafo.
            self.adiciona_arco(u, v)
            # Retorna True.
            return True
        # Adiciona a aresta no grafo.
        self.adiciona_arco(u, v)
        # Retorna False.
        return False

    def eh_conexo(self):
        """ Retorna True se o grafo é conexo. """
        # Inicializa a árvore de busca em largura.
        arvore = self.busca_largura(self.get_vertices()[0])
        # Se a árvore possui todos os vértices do grafo.
        if len(arvore) == len(self.get_vertices()):
            # Retorna True.
            return True
        # Retorna False.
        return False

    def tarjan(self):
        """ Retorna as componentes fortemente conexas do grafo. """
        # Inicializa a lista de componentes fortemente conexas.
        componentes = []
        # Inicializa a lista de vértices visitados.
        visitados = []
        # Inicializa a lista de vértices.
        pilha = []
        # Inicializa o índice.
        indice = 0
        # Para cada vértice do grafo.
        for v in self.get_vertices():
            # Se o vértice ainda não foi visitado.
            if v not in visitados:
                # Chama a função auxiliar.
                componentes, visitados, pilha, indice = self.tarjan_aux(v, componentes, visitados, pilha, indice)
        # Retorna a lista de componentes fortemente conexas.
        return componentes

    def tarjan_aux(self, v, componentes, visitados, pilha, indice):
        """ Retorna as componentes fortemente conexas do grafo. """
        # ERRO NO INDICE
        # Inicializa o índice do vértice.
        self.indices[v] = indice
        # Inicializa o índice mínimo do vértice.
        self.minimos[v] = indice
        # Incrementa o índice.
        indice += 1
        # Adiciona o vértice na lista de visitados.
        visitados.append(v)
        # Adiciona o vértice na pilha.
        pilha.append(v)
        # Para cada vértice adjacente ao vértice atual.
        for w in self.vertices_adjacentes(v):
            # Se o vértice ainda não foi visitado.
            if w not in visitados:
                # Chama a função auxiliar.
                componentes, visitados, pilha, indice = self.tarjan_aux(w, componentes, visitados, pilha, indice)
                # Atualiza o índice mínimo do vértice.
                self.minimos[v] = min(self.minimos[v], self.minimos[w])
            # Se o vértice ainda está na pilha.
            elif w in pilha:
                # Atualiza o índice mínimo do vértice.
                self.minimos[v] = min(self.minimos[v], self.indices[w])
        # Se o índice do vértice é igual ao índice mínimo do vértice.
        if self.indices[v] == self.minimos[v]:
            # Inicializa a componente fortemente conexa.
            componente = []
            # Enquanto o vértice não for o vértice atual.
            while pilha[-1] != v:
                # Adiciona o vértice na componente.
                componente.append(pilha.pop())
            # Adiciona o vértice na componente.
            componente.append(pilha.pop())
            # Adiciona a componente na lista de componentes.
            componentes.append(componente)
        # Retorna a lista de componentes fortemente conexas.
        return componentes, visitados, pilha, indice

    def print_grafo(self):
        """ Imprime o grafo. """
        print(self.__str__())

    def __len__(self):
        """ Retorna o número de vértices do grafo. """
        return len(self.adj)

    def __str__(self):
        """ Retorna a representação do grafo. """
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        """ Retorna a lista de vértices adjacentes ao vértice 'v'. """
        return self.adj[v]
