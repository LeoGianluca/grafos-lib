import unittest

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
        arestas = 8
        grafo = module.GraphProcessor.criacao_grafo_x_vertices(self, 4)

        arestas_remover = grafo.get_arestas()[0]
        arestas_remover = str(arestas_remover).replace(' ', '')
        arestas_remover = str(arestas_remover).replace(',', ';')
        arestas_remover = str(arestas_remover).replace('(', '')
        arestas_remover = str(arestas_remover).replace(')', '')

        print(arestas_remover)
        # module.GraphProcessor.remocao_arestas(self, arestas_remover)
        module.GraphProcessor.remocao_arestas(self, '(12;13)')
        # self.assertEqual(len(grafo.get_arestas()), 1)


if __name__ == '__main__':
    unittest.main()
