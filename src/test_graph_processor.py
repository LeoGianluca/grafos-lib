import unittest
import argparse

import graph_processor as module


class TestGraphProcessor(unittest.TestCase):
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
        pass

    def test_ponderacao_arestas(self):
        pass

    def test_rotulacao_arestas(self):
        pass

    def test_checagem_adjacencia_vertices(self):
        pass

    def test_checagem_adjacencia_arestas(self):
        pass

    def test_checagem_existencia_arestas(self):
        pass

    def test_checagem_quantidade_vertices(self):
        pass

    def test_checagem_quantidade_arestas(self):
        pass

    def test_checagem_grafo_vazio(self):
        pass

    def test_checagem_grafo_completo(self):
        pass

    def test_naive(self):
        pass

    def test_fleury(self):
        pass

    def test_tarjan(self):
        pass


if __name__ == '__main__':
    unittest.main()
