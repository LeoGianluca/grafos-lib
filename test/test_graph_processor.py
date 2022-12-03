from unittest import TestCase
import src.graph as graph
import src.graph_processor as graph_processor


class TestGraphProcessor(TestCase):
    def test_criacao_grafo_x_vertices(self):
        vertices = 4
        arestas = graph_processor.GraphProcessor.criacao_grafo_x_vertices(vertices)
        self.assertEqual(len(graph.arestas), vertices)

