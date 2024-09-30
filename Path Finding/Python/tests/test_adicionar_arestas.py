from src.dijkstra import Grafo


def test_adicionar_arestas():
    grafo = Grafo([[] for _ in range(10)])
    grafo.adicionar_arestas(0, "N", 2)
    assert grafo.matriz_adj[0] == [("V0", "N", 2)]