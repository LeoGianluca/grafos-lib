import unittest
import argparse

import graph_processor as module
from src.file_processor import FileProcessor


class TestGraphProcessor(unittest.TestCase):

    file_processor = FileProcessor()

    def test_criacao_grafo_x_vertices(self):
        vertices = 4
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, vertices)
        self.assertEqual(len(grafo.get_vertices()), vertices)

    def test_criacao_arestas(self):
        arestas = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, arestas)
        self.assertEqual(len(grafo.get_arestas()), 11)

    def test_remocao_arestas(self):
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        arestas = grafo.get_arestas()[0]

        aresta_a = arestas[0]
        aresta_b = arestas[1]
        join_arestas = "%s;%s" % (aresta_a, aresta_b)

        module.GraphProcessor.remocao_arestas(self, join_arestas)

    def test_rotulacao_vertices(self):
        pass

    def test_ponderacao_vertices(self):
        file_in = 'data/in/teste-matriz-1.csv'
        self.file_processor.read_file_matrix(file_in)
        # graph_info = [['A', 'B', 4], ['A', 'C', 3], ['A', 'D', 2], ['A', 'E', 1]]

        module.GraphProcessor.criacao_grafo_x_vertices(self, 4)

    def test_ponderacao_arestas(self):
        pass

    def test_rotulacao_arestas(self):
        pass

    def test_checagem_adjacencia_vertices(self):
        vertices = 4
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, vertices)
        module.GraphProcessor.criacao_arestas(self, 8)

        vertices = grafo.get_vertices()[0]

        module.GraphProcessor.checagem_adjacencia_vertices(self, vertices)

    def test_checagem_adjacencia_arestas(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        arestas = grafo.get_arestas()[0]

        module.GraphProcessor.checagem_adjacencia_arestas(self, arestas)

    def test_checagem_existencia_arestas(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        arestas = grafo.get_arestas()[0]

        aresta_a = arestas[0]
        aresta_b = arestas[1]
        join_arestas = "%s;%s" % (aresta_a, aresta_b)

        module.GraphProcessor.checagem_existencia_arestas(self, join_arestas)

    def test_checagem_quantidade_vertices(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        module.GraphProcessor.checagem_quantidade_vertices(self)

    def test_checagem_quantidade_arestas(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        module.GraphProcessor.checagem_quantidade_arestas(self)

    def test_checagem_grafo_vazio(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        module.GraphProcessor.checagem_grafo_vazio(self)

    def test_checagem_grafo_completo(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        module.GraphProcessor.checagem_grafo_completo(self)

    def test_naive(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        vertice = grafo.get_vertices()[0]

        module.GraphProcessor.naive(self, vertice)

    def test_fleury(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        vertice = grafo.get_vertices()[0]

        module.GraphProcessor.fleury(self, vertice)

    def test_tarjan(self):
        vertice = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)
        module.GraphProcessor.criacao_arestas(self, vertice)

        module.GraphProcessor.tarjan(self)


if __name__ == '__main__':
    unittest.main()
