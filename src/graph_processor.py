from collections import defaultdict
import random

# from graph import Grafo
import graph


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content):
        self.input_format = input_format  # Formato de entrada
        self.input_content = input_content  # Conteúdo de entrada
        self.adj = defaultdict(set)  # Dicionário de adjacências
        if input_content is not None:  # Se o conteúdo de entrada não for nulo
            self.grafo = graph.Grafo(input_content)  # Cria um grafo com o conteúdo de entrada
        else:  # Se o conteúdo de entrada for nulo
            self.grafo = None  # O grafo é nulo

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        # Gerando um grafo com x vértices aleatóriamente com letras de A a Z não repetidas
        vertices = []  # Lista de vértices
        for i in range(0, int(extra_args)):  # Para cada vértice
            random_number = random.randint(1, 11000)  # Gera um número aleatório entre 1 e 11000
            if random_number not in vertices:  # Se o número não estiver nos vértices
                vertices.append(random_number)  # Adiciona o número aos vértices
            else:  # Se o número estiver nos vértices
                random_number = random.randint(1, 11000)  # Gera um novo número aleatório entre 1 e 11000
                vertices.append(random_number)  # Adiciona o novo número aos vértices

        # Víncula os vertices ao primeiro vertice
        arestas = []  # Lista de arestas
        for i in range(1, len(vertices)):  # Para cada vértice
            arestas.append((vertices[0], vertices[i]))  # Adiciona uma aresta entre o primeiro vértice e o vértice atual

        # Cria e imprime o grafo. O grafo é criado com os vértices e as arestas
        self.grafo = graph.Grafo(vertices, arestas, direcionado=True)  # Cria um grafo com as arestas e direcionado
        return self.grafo  # Retorna o grafo

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        arestas = self.grafo.get_arestas()  # Pega as arestas do grafo
        novas_arestas = []  # Lista de novas arestas
        for i in range(0, int(extra_args)):  # Para cada aresta
            random_number = random.randint(1, 11000)  # Gera um número aleatório entre 1 e 11000
            if random_number not in arestas:  # Se o número não estiver nas arestas
                novas_arestas.append([i, random_number])  # Adiciona o número às novas arestas
            else:  # Se o número estiver nas arestas
                random_number = random.randint(1, 11000)  # Gera um novo número aleatório entre 1 e 11000
                novas_arestas.append([i, random_number])  # Adiciona o novo número às novas arestas

        self.grafo.adiciona_arestas(novas_arestas)  # Adiciona as novas arestas ao grafo

    def remocao_arestas(self, extra_args):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")

        if extra_args.find("|") != -1:  # Se o extra_args tiver um |
            extra_args = extra_args.split("|")  # Separa os argumentos
            print('entrou no if')

        for extra_arg in extra_args:  # Para cada argumento
            print('entrou no for', extra_args)
            aux = extra_arg.split(";")  # Separa o argumento
            self.grafo.remove_arco(aux[0], aux[1])  # Remove o arco

    def rotulacao_vertices(self, extra_args):
        print(f"Execuntando 'rotulacao_vertices' [extra_args={extra_args}]")
        self.grafo.rotula_vertices(extra_args)  # Rotula os vértices

    def ponderacao_vertices(self):
        print(f"Execuntando 'ponderacao_vertices'")
        pondera = self.grafo.pondera_vertices()

    def ponderacao_arestas(self, extra_args):
        print(f"Execuntando 'ponderacao_arestas' [extra_args={extra_args}]")
        self.grafo.pondera_arestas(extra_args)  # Pondera as arestas

    def componentes_conexas(self):
        print(f"Execuntando 'componentes_conexas'")
        self.grafo.componentes_conexas()  # Componentes conexas

    def rotulacao_arestas(self, extra_args):
        print(f"Execuntando 'rotulacao_arestas' [extra_args={extra_args}]")
        self.grafo.rotula_arestas(extra_args)  # Rotula as arestas

    def checagem_adjacencia_vertices(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_vertices' [extra_args={extra_args}]")

        adjacentes = self.grafo.vertices_adjacentes(extra_args)  # Pega os vértices adjacentes

        print(f"Adjacentes ao vertice {extra_args}: ", adjacentes)  # Imprime os vértices adjacentes

    def checagem_adjacencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_arestas' [extra_args={extra_args}]")

        adjacentes = self.grafo.arestas_adjacentes(extra_args)  # Pega as arestas adjacentes

        print(f"Adjacentes a aresta {extra_args}: ", adjacentes)  # Imprime as arestas adjacentes

    def checagem_existencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_existencia_arestas' [extra_args={extra_args}]")

        extra_args = extra_args.split(";")  # Separa os argumentos

        arestas = self.grafo.existe_aresta(extra_args[0], extra_args[1])  # Pega as arestas

        print(
            f"Existe aresta entre {extra_args[0]} e {extra_args[1]}? {arestas}")  # Imprime se existe aresta entre os vértices

    def checagem_quantidade_vertices(self):
        print(f"Execuntando 'checagem_quantidade_vertices'")

        print(f"Quantidade de vertices: {len(self.grafo.get_vertices())}")  # Imprime a quantidade de vértices

    def checagem_quantidade_arestas(self):  # Imprime a quantidade de arestas
        print(f"Execuntando 'checagem_quantidade_arestas'")

        print(f"Quantidade de arestas: {len(self.grafo.get_arestas())}")  # Imprime a quantidade de arestas

    def checagem_grafo_vazio(self):
        print(f"Execuntando 'checagem_grafo_vazio'")

        if not self.grafo.get_arestas():  # Se não houver arestas
            print("Grafo vazio")  # Imprime que o grafo está vazio
        else:  # Se houver arestas
            print("Grafo não vazio")  # Imprime que o grafo não está vazio

    def checagem_grafo_completo(self):
        print(f"Execuntando 'checagem_grafo_completo'")

        if self.grafo.grafo_completo():  # Se o grafo for completo
            print("Grafo completo")  # Imprime que o grafo é completo
        else:  # Se o grafo não for completo
            print("Grafo não completo")  # Imprime que o grafo não é completo

    def caminho_minimo(self, extra_args):
        print(f"Execuntando 'caminho_minimo' [extra_args={extra_args}]")
        self.grafo.caminho_minimo(extra_args)  # Caminho mínimo

    def naive(self):
        print(f"Execuntando 'naive'")

        self.grafo.naive()  # Executa o algoritmo naive

    def fleury(self):
        print(f"Execuntando 'fleury'")
        self.grafo.fleury()  # Executa o Algoritmo de

    def tarjan(self):
        print(f"Execuntando 'tarjan'")
        self.grafo.tarjan()  # Executa o Algoritmo de Tarjan
