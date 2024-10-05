from src.dijkstra import Grafo

matriz_lista_adjacencia = [
    [],
    [("V0", "O", 1), ("V2", "L", 1), ("V7", "S", 1)],
    [],
    [("V4", "L", 1), ("V9", "S", 1)],
    [],
    [("V6", "L", 1), ("V11", "S", 1)],
    [("V5", "O", 1)],
    [("V1", "N", 1), ("V8", "L", 1), ("V14", "S", 1)],
    [("V7", "O", 1), ("V2", "N", 1), ("V9", "L", 1)],
    [("V8", "O", 1), ("V3", "N", 1), ("V10", "L", 1), ("V16", "S", 1)],
    [("V9", "O", 1), ("V4", "N", 1), ("V17", "S", 1), ("V11", "L", 1)],
    [("V10", "O", 1), ("V12", "L", 1), ("V5", "N", 1), ("V18", "S", 1)],
    [("V11", "O", 1)],
    [],
    [("V13", "O", 1), ("V15", "L", 1), ("V20", "S", 1), ("V7", "N", 1)],
    [],
    [("V15", "O", 1), ("V9", "N", 1), ("V22", "S", 1)],
    [],
    [("V11", "N", 1), ("V19", "L", 1), ("V24", "S", 1)],
    [("V18", "O", 1)],
    [("V14", "N", 1), ("V21", "L", 1), ("V27", "S", 1)],
    [("V28", "S", 1), ("V22", "L", 1),("V20","O",1)],
    [("V21", "O", 1), ("V23", "L", 1), ("V29", "S", 1),("V16","N",1)],
    [("V22", "O", 1), ("V17", "N", 1), ("V30", "S", 1), ("V24", "L", 1)],
    [("V23", "O", 1), ("V25", "L", 1), ("V31", "S", 1),("V18","N",1)],
    [("V24", "O", 1)],
    [],
    [("V26", "O", 1), ("V20", "N", 1)],
    [],
    [("V28", "O", 1), ("V22", "N", 1)],
    [],
    [("V30", "O", 1), ("V32", "L", 1), ("V24", "N", 1)],
    [("V31", "O", 1)]
]

def test_dijkstra_menor_caminho():
    grafo = Grafo(matriz_lista_adjacencia)
    caminho, distancia, direcoes = grafo.dijkstra(1, 9)
    assert caminho == [1, 7, 8, 9]

def test_mostrar_matriz(capsys):
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.mostrar_matriz()
    captured = capsys.readouterr()
    assert "('V0', 'O', 1)" in captured.out
    assert "('V11', 'S', 1)" in captured.out

def test_adicionar_arestas():
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.adicionar_arestas(10, 0, "N", 2)
    assert grafo.matriz_adj[10] == [("V9", "O", 1), ("V4", "N", 1), ("V17", "S", 1), ("V11", "L", 1),("V0", "N", 2)] # Adiciona ao final da lista por conta do append

def test_remover_arestas():
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.remover_arestas(8,2)
    assert grafo.matriz_adj[8] == [("V7", "O", 1), ("V9", "L", 1)]

