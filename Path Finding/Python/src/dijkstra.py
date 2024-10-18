import heapq

TAM_ROBO_DIVIDIDO_POR_DOIS = 7.7

class Grafo:
    def __init__(self, matriz_lista_adjacencia):
        self.num_vertices = len(matriz_lista_adjacencia)
        self.obstaculos = []

    def adicionar_arestas(self, origem, destino, direcao, peso=1):
        matriz_lista_adjacencia[origem].append([f"V{destino}", f"{direcao}", peso])

    def remover_arestas(self, origem, destino):
        vertice = "V" + str(destino)
        for indice, items in enumerate(matriz_lista_adjacencia[origem]):
            if items[0] == vertice:
                matriz_lista_adjacencia[origem].pop(indice)

    def mostrar_matriz(self, matriz):
        for linha in matriz:
            print(linha)

    def marcar_obstaculo(self, vertice):
        for linha in matriz_obstaculos:
            for aresta in linha:
                if str(aresta[0]).strip() == vertice:
                    aresta[-1] = float('inf')
        self.obstaculos.append(vertice)
    
    def desmarcar_obstaculo(self, vertice): 
        for linha in matriz_obstaculos:
            for index_aresta, aresta in enumerate(linha):
                if str(aresta[0]).strip() == vertice:
                    index = linha[0][0]
                    matriz_obstaculos[index][index_aresta] = [aresta[0], aresta[1], matriz_lista_adjacencia[index][index_aresta][2]]
        self.mostrar_matriz(matriz_obstaculos)

    def dijkstra(self, inicio, fim):
        distancias = {i: float('inf') for i in range(self.num_vertices)}
        distancias[inicio] = 0
        heap = [(0, inicio)]  
        anterior = {i: None for i in range(self.num_vertices)}
        direcao = {i: None for i in range(self.num_vertices)}
        pesos = {i: None for i in range(self.num_vertices)}  

        while heap:
            dist_atual, vertice_atual = heapq.heappop(heap)

            if vertice_atual == fim:
                break   

            if dist_atual > distancias[vertice_atual]:
                continue

            for vizinho_info in matriz_obstaculos[vertice_atual]:
                if len(vizinho_info) == 3: 
                    vizinho, dir_cardinal, peso = vizinho_info  
                    vizinho_num = int(vizinho[1:])  

                    if peso == float('inf'): 
                        continue


                    nova_distancia = dist_atual + peso

                    if nova_distancia < distancias[vizinho_num]:
                        distancias[vizinho_num] = nova_distancia
                        anterior[vizinho_num] = vertice_atual
                        direcao[vizinho_num] = dir_cardinal 
                        pesos[vizinho_num] = peso
                        heapq.heappush(heap, (nova_distancia, vizinho_num))

        caminho = []
        direcoes_pesos = []
        if distancias[fim] != float('inf'):
            atual = fim
            while atual is not None:
                caminho.append(atual)
                if anterior[atual] is not None:
                    direcoes_pesos.append((direcao[atual], pesos[atual]))
                atual = anterior[atual]
            caminho.reverse()
            direcoes_pesos.reverse()

        return caminho, distancias[fim], direcoes_pesos

    def recalcular_caminho_sem_obstaculos(self, inicio, fim):
        for vertice in self.obstaculos:
            self.desmarcar_obstaculo(vertice) 
            caminho, distancia, _ = self.dijkstra(inicio, fim)
            if distancia != float('inf'):
                return caminho, distancia
        return None, float('inf')


matriz_lista_adjacencia = [
    [[0]],
    [[1],["V0", "O", 24], ["V2", "L", 30], ["V7", "S", 30]],
    [[2]],
    [[3],["V4", "L", 30], ["V9", "S", 30]],
    [[4]],
    [[5],["V6", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V11", "S", 30]],
    [[6],["V5", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[7],["V1", "N", 30], ["V8", "L", 30], ["V14", "S", 30]],
    [[8],["V7", "O", 30], ["V2", "N", 30], ["V9", "L", 30]],
    [[9],["V8", "O", 30], ["V3", "N", 30], ["V10", "L", 30], ["V16", "S", 30]],
    [[10],["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30]],
    [[11],["V10", "O", 1], ["V12", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V5", "N", 30], ["V18", "S", 30]],
    [[12],["V11", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[13]],
    [[14],["V13", "O", 24], ["V15", "L", 30], ["V20", "S", 30], ["V7", "N", 30]],
    [[15]],
    [[16],["V15", "O", 30], ["V9", "N", 30], ["V22", "S", 30]],
    [[17]],
    [[18],["V11", "N", 30], ["V19", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "S", 30]],
    [[19],["V18", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[20],["V14", "N", 30], ["V21", "L", 30], ["V27", "S", 30]],
    [[21],["V28", "S", 30], ["V22", "L", 30], ["V20", "O", 30]],
    [[22],["V21", "O", 30], ["V23", "L", 30], ["V29", "S", 30], ["V16", "N", 30]],
    [[23],["V22", "O", 30], ["V17", "N", 30], ["V30", "S", 30], ["V24", "L", 30]],
    [[24],["V23", "O", 30], ["V25", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V31", "S", 30], ["V18", "N", 30]],
    [[25],["V24", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[26]],
    [[27],["V26", "O", 24], ["V20", "N", 30]],
    [[28]],
    [[29],["V28", "O", 30], ["V22", "N", 30]],
    [[30]],
    [[31],["V30", "O", 30], ["V32", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "N", 30]],
    [[32],["V31", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
]

matriz_obstaculos = [
    [[0]],
    [[1],["V0", "O", 24], ["V2", "L", 30], ["V7", "S", 30]],
    [[2]],
    [[3],["V4", "L", 30], ["V9", "S", 30]],
    [[4]],
    [[5],["V6", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V11", "S", 30]],
    [[6],["V5", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[7],["V1", "N", 30], ["V8", "L", 30], ["V14", "S", 30]],
    [[8],["V7", "O", 30], ["V2", "N", 30], ["V9", "L", 30]],
    [[9],["V8", "O", 30], ["V3", "N", 30], ["V10", "L", 30], ["V16", "S", 30]],
    [[10],["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30]],
    [[11],["V10", "O", 1], ["V12", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V5", "N", 30], ["V18", "S", 30]],
    [[12],["V11", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[13]],
    [[14],["V13", "O", 24], ["V15", "L", 30], ["V20", "S", 30], ["V7", "N", 30]],
    [[15]],
    [[16],["V15", "O", 30], ["V9", "N", 30], ["V22", "S", 30]],
    [[17]],
    [[18],["V11", "N", 30], ["V19", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "S", 30]],
    [[19],["V18", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[20],["V14", "N", 30], ["V21", "L", 30], ["V27", "S", 30]],
    [[21],["V28", "S", 30], ["V22", "L", 30], ["V20", "O", 30]],
    [[22],["V21", "O", 30], ["V23", "L", 30], ["V29", "S", 30], ["V16", "N", 30]],
    [[23],["V22", "O", 30], ["V17", "N", 30], ["V30", "S", 30], ["V24", "L", 30]],
    [[24],["V23", "O", 30], ["V25", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V31", "S", 30], ["V18", "N", 30]],
    [[25],["V24", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [[26]],
    [[27],["V26", "O", 24], ["V20", "N", 30]],
    [[28]],
    [[29],["V28", "O", 30], ["V22", "N", 30]],
    [[30]],
    [[31],["V30", "O", 30], ["V32", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V24", "N", 30]],
    [[32],["V31", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
]

def main():
    inicio = 20
    fim = 6

    grafo = Grafo(matriz_lista_adjacencia)

    grafo.marcar_obstaculo("V5")
    grafo.mostrar_matriz(matriz_obstaculos)
    
    caminho, distancia, direcoes_pesos = grafo.dijkstra(inicio, fim)
    
    if distancia != float('inf'):
        print(f"Os vértices visitados são: {caminho}")
        print(f"A distância mínima calculada vale: {distancia}")
        print(f"A saída que o Zé pediu: {direcoes_pesos}")
    else:
        print("Caminho bloqueado, tentando remover obstáculos.")
        caminho, distancia = grafo.recalcular_caminho_sem_obstaculos(inicio, fim)
        if distancia != float('inf'):
            print(f"Caminho após remover obstáculos: {caminho}")
            print(f"A distância mínima recalculada vale: {distancia}")
        else:
            print("Não foi possível encontrar um caminho, mesmo sem os obstáculos.")

main()