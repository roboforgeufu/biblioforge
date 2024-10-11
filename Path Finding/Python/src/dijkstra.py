import heapq

"""
Esse código usa a classe de grafo para criar métodos de manipulação de um grafo. Vale ressaltar que ele é um grafo direcionado, 
ou seja, não existe vértice que volta do estabelecimento pela linha amarela. Deixei assim para que seja possível fazer as tratativas depois.
Todos os pesos estão unitários, apenas na inicialização que as distâncias são tratadas como infinitas (característica do algoritmo).
"""

# TODO fazer tratativa para obstáculos
# TODO fazer com que o obstáculo seja desmarcado quando eu não consigo achar mais o caminho

TAM_ROBO_DIVIDIDO_POR_DOIS = 7.7

class Grafo:
    def __init__(self, matriz_lista_adjacencia, matriz_obstaculos):
        self.num_vertices = len(matriz_lista_adjacencia)
        self.matriz_adj = matriz_lista_adjacencia
        self.matriz_obs = matriz_obstaculos
        self.obstaculos = []
        self.valores_antigos = {}  

    def adicionar_arestas(self, origem, destino, direcao, peso=1):
        self.matriz_adj[origem].append([f"V{destino}", f"{direcao}", peso])

    def remover_arestas(self, origem, destino):
        vertice = "V" + str(destino)
        for indice, items in enumerate(self.matriz_adj[origem]):
            primeiro_item = items[0]
            if primeiro_item == vertice:
                print(self.matriz_adj[origem])
                self.matriz_adj[origem].pop(indice)

    def mostrar_matriz(self, matriz):
        for linha in matriz:
            print(linha)

    def marcar_obstaculo(self, vertice):
        for linha in self.matriz_obs:
            for aresta in linha:
                if str(aresta[0]).strip() == vertice:
                    aresta[2] = 100000
                    self.obstaculos.append([vertice, aresta])

    def desmarcar_obstaculo(self, vertice):
        ...


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

            for vizinho_info in self.matriz_adj[vertice_atual]:
                vizinho, dir_cardinal, peso = vizinho_info  
                vizinho_num = int(vizinho[1:])  

                if vizinho in self.obstaculos:  
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
    [],
    [["V0", "O", 24], ["V2", "L", 30], ["V7", "S", 30]],
    [],
    [["V4", "L", 30], ["V9", "S", 30]],
    [],
    [["V6", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V11", "S", 30]],
    [["V5", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [["V1", "N", 30], ["V8", "L", 30], ["V14", "S", 30]],
    [["V7", "O", 30], ["V2", "N", 30], ["V9", "L", 30]],
    [["V8", "O", 30], ["V3", "N", 30], ["V10", "L", 30], ["V16", "S", 30]],
    [["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30]],
    [["V10", "O", 1], ["V12", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V5", "N", 30], ["V18", "S", 30]],
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

matriz_obstaculos = [
    [1],
    [["V0", "O", 24], ["V2", "L", 30], ["V7", "S", 30]],
    [],
    [["V4", "L", 30], ["V9", "S", 30]],
    [],
    [["V6", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V11", "S", 30]],
    [["V5", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]],
    [["V1", "N", 30], ["V8", "L", 30], ["V14", "S", 30]],
    [["V7", "O", 30], ["V2", "N", 30], ["V9", "L", 30]],
    [["V8", "O", 30], ["V3", "N", 30], ["V10", "L", 30], ["V16", "S", 30]],
    [["V9", "O", 30], ["V4", "N", 30], ["V17", "S", 30], ["V11", "L", 30]],
    [["V10", "O", 1], ["V12", "L", 18-TAM_ROBO_DIVIDIDO_POR_DOIS], ["V5", "N", 30], ["V18", "S", 30]],
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
    [["V31", "O", 18-TAM_ROBO_DIVIDIDO_POR_DOIS]]
]


matriz_obstaculos = matriz_lista_adjacencia

def main():
    
    inicio = 20
    fim = 6

    grafo = Grafo(matriz_lista_adjacencia,matriz_obstaculos)


    grafo.marcar_obstaculo("V5")
    grafo.mostrar_matriz(matriz_obstaculos)

    caminho, distancia, direcoes_pesos = grafo.dijkstra(inicio,fim)
    
    if distancia != float('inf'):
        print()
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