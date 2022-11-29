from collections import defaultdict
import random

from graph import Grafo


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content):
        self.input_format = input_format
        self.input_content = input_content
        self.adj = defaultdict(set)
        if input_content is not None:
            self.grafo = Grafo(input_content)
        else:
            self.grafo = None

        self.grafo.print_grafo()

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        # Gerando um grafo com x vértices aleatóriamente com letras de A a Z não repetidas
        vertices = []
        for i in range(0, int(extra_args)):
            random_number = random.randint(1, 10000)
            if random_number not in vertices:
                vertices.append(random_number)
            else:
                random_number = random.randint(1, 1000)
                vertices.append(random_number)

        print("Vertices: ", vertices)

        # Víncula os vertices ao primeiro vertice
        arestas = []
        for i in range(1, len(vertices)):
            arestas.append((vertices[0], vertices[i]))

        # Cria e imprime o grafo.
        self.grafo = Grafo(arestas, direcionado=True)
        print(self.grafo)

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        arestas = self.grafo.get_arestas()
        novas_arestas = []
        for i in range(0, int(extra_args)):
            random_number = random.randint(1, 10000)
            if random_number not in arestas:
                novas_arestas.append([i, random_number])
            else:
                random_number = random.randint(1, 1000)
                novas_arestas.append([i, random_number])

        print("Arestas Originais: ", arestas)
        print("Arestas Novas: ", novas_arestas)

        self.grafo.adiciona_arestas(novas_arestas)

    def remocao_arestas(self, extra_args):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")

        extra_args = extra_args.split("|")
        print(extra_args)

        for extra_arg in extra_args:
            aux = extra_arg.split(";")
            self.grafo.remove_arco(aux[0], aux[1])

    def rotulacao_vertices(self):
        print(f"Execuntando 'rotulacao_vertices'")
        print(self.input_content)
        pass

    def ponderacao_vertices(self):
        print(f"Execuntando 'ponderacao_vertices'")
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
