from src.dijkstra import Grafo, TAM_ROBO_DIVIDIDO_POR_DOIS, matriz_lista_adjacencia, matriz_obstaculos

def test_dijkstra():
    grafo = Grafo(matriz_lista_adjacencia)
    caminho, distancia, direcoes = grafo.dijkstra(1, 9)
    assert caminho == [1, 7, 8, 9]

def test_marcar_obstaculo():
    grafo = Grafo(matriz_lista_adjacencia)  
    grafo.marcar_obstaculo("V5")  

    matriz_esperada = [
        [[0]],
        [[1], ['V0', 'O', 24], ['V2', 'L', 30], ['V7', 'S', 30]],
        [[2]],
        [[3], ['V4', 'L', 30], ['V9', 'S', 30]],
        [[4]],
        [[5], ['V6', 'L', 10.3], ['V11', 'S', 30]],
        [[6], ['V5', 'O', float("inf")]],
        [[7], ['V1', 'N', 30], ['V8', 'L', 30], ['V14', 'S', 30]],
        [[8], ['V7', 'O', 30], ['V2', 'N', 30], ['V9', 'L', 30]],
        [[9], ['V8', 'O', 30], ['V3', 'N', 30], ['V10', 'L', 30], ['V16', 'S', 30]],
        [[10], ['V9', 'O', 30], ['V4', 'N', 30], ['V17', 'S', 30], ['V11', 'L', 30]],
        [[11], ['V10', 'O', 1], ['V12', 'L', 10.3], ['V5', 'N', float("inf")], ['V18', 'S', 30]],
        [[12], ['V11', 'O', 10.3]],
        [[13]],
        [[14], ['V13', 'O', 24], ['V15', 'L', 30], ['V20', 'S', 30], ['V7', 'N', 30]],
        [[15]],
        [[16], ['V15', 'O', 30], ['V9', 'N', 30], ['V22', 'S', 30]],
        [[17]],
        [[18], ['V11', 'N', 30], ['V19', 'L', 10.3], ['V24', 'S', 30]],
        [[19], ['V18', 'O', 10.3]],
        [[20], ['V14', 'N', 30], ['V21', 'L', 30], ['V27', 'S', 30]],
        [[21], ['V28', 'S', 30], ['V22', 'L', 30], ['V20', 'O', 30]],
        [[22], ['V21', 'O', 30], ['V23', 'L', 30], ['V29', 'S', 30], ['V16', 'N', 30]],
        [[23], ['V22', 'O', 30], ['V17', 'N', 30], ['V30', 'S', 30], ['V24', 'L', 30]],
        [[24], ['V23', 'O', 30], ['V25', 'L', 10.3], ['V31', 'S', 30], ['V18', 'N', 30]],
        [[25], ['V24', 'O', 10.3]],
        [[26]],
        [[27], ['V26', 'O', 24], ['V20', 'N', 30]],
        [[28]],
        [[29], ['V28', 'O', 30], ['V22', 'N', 30]],
        [[30]],
        [[31], ['V30', 'O', 30], ['V32', 'L', 10.3], ['V24', 'N', 30]],
        [[32], ['V31', 'O', 10.3]]
    ]

    assert matriz_obstaculos == matriz_esperada 


def test_desmarcar_obstaculo():
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.desmarcar_obstaculo("V5")
    grafo.mostrar_matriz(matriz_obstaculos)
    assert matriz_obstaculos == matriz_lista_adjacencia
    
def test_adicionar_arestas():
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.adicionar_arestas(10, 0, "N", 2)
    assert matriz_lista_adjacencia[10] == [[10],["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30], ["V0","N",2]]

def test_remover_arestas():
    grafo = Grafo(matriz_lista_adjacencia)
    grafo.remover_arestas(8,2)
    assert matriz_lista_adjacencia[8] == [[8],["V7", "O", 30], ["V9", "L", 30]]
    matriz_lista_adjacencia.insert(2, [2,"N",30])
    
