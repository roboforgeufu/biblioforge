from src.dijkstra import Grafo, TAM_ROBO_DIVIDIDO_POR_DOIS, matriz_lista_adjacencia, matriz_obstaculos

def test_dijkstra():
    grafo = Grafo(matriz_lista_adjacencia, matriz_obstaculos)
    caminho, distancia, direcoes = grafo.dijkstra(1, 9)
    assert caminho == [1, 7, 8, 9]
    
def test_adicionar_arestas():
    grafo = Grafo(matriz_lista_adjacencia, matriz_obstaculos)
    grafo.adicionar_arestas(10, 0, "N", 2)
    assert grafo.matriz_adj[10] == [['V9', 'O', 30], ['V4', 'N', 30], ['V17', 'S', 30], ['V11', 'L', 30], ['V0', 'N', 2]]

def test_remover_arestas():
    grafo = Grafo(matriz_lista_adjacencia, matriz_obstaculos)
    grafo.remover_arestas(8,2)
    print(grafo.matriz_adj)
    assert grafo.matriz_adj[8] == [["V7", "O", 30], ["V9", "L", 30]]
    grafo.matriz_adj.insert(2, [2,"N",30])
    

def test_marcar_obstaculo():
    grafo = Grafo(matriz_lista_adjacencia, matriz_obstaculos)
    grafo.marcar_obstaculo("V5")   
    matriz_esperada = [
    [],
    [["V0", "O", 24], ["V2", "L", 30], ["V7", "S", 30]],
    [],
    [["V4", "L", 30], ["V9", "S", 30]],
    [],
    [["V6", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V11", "S", 30]],
    [["V5", "O", 100000]],
    [["V1", "N", 30], ["V8", "L", 30], ["V14", "S", 30]],
    [["V7", "O", 30], ["V2", "N", 30], ["V9", "L", 30]],
    [["V8", "O", 30], ["V3", "N", 30], ["V10", "L", 30], ["V16", "S", 30]],
    [["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30]],
    [["V10", "O", 1], ["V12", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V5", "N", 100000], ["V18", "S", 30]],
    [["V11", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [],
    [["V13", "O", 24], ["V15", "L", 30], ["V20", "S", 30], ["V7", "N", 30]],
    [],
    [["V15", "O", 30], ["V9", "N", 30], ["V22", "S", 30]],
    [],
    [["V11", "N", 30], ["V19", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "S", 30]],
    [["V18", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [["V14", "N", 30], ["V21", "L", 30], ["V27", "S", 30]],
    [["V28", "S", 30], ["V22", "L", 30], ["V20", "O", 30]],
    [["V21", "O", 30], ["V23", "L", 30], ["V29", "S", 30], ["V16", "N", 30]],
    [["V22", "O", 30], ["V17", "N", 30], ["V30", "S", 30], ["V24", "L", 30]],
    [["V23", "O", 30], ["V25", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V31", "S", 30], ["V18", "N", 30]],
    [["V24", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [],
    [["V26", "O", 24], ["V20", "N", 30]],
    [],
    [["V28", "O", 30], ["V22", "N", 30]],
    [],
    [["V30", "O", 30], ["V32", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "N", 30]],
    [["V31", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
]
        
    
    assert grafo.matriz_obstaculos == matriz_esperada


def test_desmarcar_obstaculo():
    grafo = Grafo(matriz_lista_adjacencia, matriz_obstaculos)
    grafo.marcar_obstaculo("V5")
    grafo.desmarcar_obstaculo("V5")
    assert grafo.matriz_obstaculos == grafo.matriz_adj
