import heapq

"""
Esse código usa a classe de grafo para criar métodos de manipulação de um grafo. Vale ressaltar que ele é um grafo direcionado, 
ou seja, não existe vértice que volta do estabelecimento pela linha amarela. Deixei assim para que seja possível fazer as tratativas depois.
Todos os pesos estão unitários, apenas na inicialização que as distâncias são tratadas como infinitas (característica do algoritmo).
"""

#TODO mudar saída para o formato combinado (peso, direção)
#TODO fazer tratativa para obstáculos
#TODO fazer com que o obstáculo seja desmarcado quando eu não consigo achar mais o caminho
#TODO colocar pesos como distâncias 

class Grafo:
    def __init__(self, matriz_lista_adjacencia):
        self.num_vertices = len(matriz_lista_adjacencia)
        self.matriz_adj = matriz_lista_adjacencia
    
    def adicionar_arestas(self, origem, destino, direcao, peso=1):
        self.matriz_adj[origem].append((f"V{destino}", f"{direcao}", peso)) 
    
    def remover_arestas(self, origem, destino):
        vertice = "V" + str(destino)
        for indice, items in enumerate(self.matriz_adj[origem]):
            primeiro_item= items[0]
            print(primeiro_item)
            if primeiro_item == vertice:
                self.matriz_adj[origem].pop(indice)

    def mostrar_matriz(self):
        for linha in self.matriz_adj:
            print(linha)

    def dijkstra_menor_caminho(self, inicio, fim):
        distancias = {i: float('inf') for i in range(self.num_vertices)}
        distancias[inicio] = 0
        # Heap para o menor caminho
        heap = [(0, inicio)]  # (distancia, vertice)
        print(f"As distâncias inicializadas são: {distancias}")
        print("")
        # Anterior e direção usada
        anterior = {i: None for i in range(self.num_vertices)}
        direcao = {i: None for i in range(self.num_vertices)}
        print(f"Os valores de anterior inicializados são: {anterior}")
        print("")
        print(f"Os valores de direçao inicializados são: {direcao}")
        
        while heap:
            dist_atual, vertice_atual = heapq.heappop(heap)

            if vertice_atual == fim:
                break   

            if dist_atual > distancias[vertice_atual]:
                continue

            # Verifica todos os vizinhos
            for vizinho_info in self.matriz_adj[vertice_atual]:
                vizinho, dir_cardinal, peso = vizinho_info  # Extrai vértice, direção e peso
                vizinho = int(vizinho[1:])  # Remove o "V" e converte para inteiro
                
                nova_distancia = dist_atual + peso  # Soma o peso da aresta

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anterior[vizinho] = vertice_atual
                    direcao[vizinho] = dir_cardinal  # Salva a direção
                    heapq.heappush(heap, (nova_distancia, vizinho))

        # Reconstrói o caminho
        caminho = []
        direcoes = []
        if distancias[fim] != float('inf'):
            atual = fim
            while atual is not None:
                caminho.append(atual)
                if anterior[atual] is not None:
                    direcoes.append(direcao[atual])
                atual = anterior[atual]
            caminho.reverse()
            direcoes.reverse()

        return caminho, distancias[fim], direcoes

    def coordenadas_consecutivas(self, direcoes):
        if not direcoes:
            return "Nenhum caminho encontrado"

        mapa = []
        direcao_atual = direcoes[0]
        contador = 1

        for i in range(1, len(direcoes)):
            if direcoes[i] == direcao_atual:
                contador += 1
            else:
                mapa.append(f"{contador}{direcao_atual}")
                direcao_atual = direcoes[i]
                contador = 1

        # Adiciona a última direção
        mapa.append(f"{contador}{direcao_atual}")

        return ",".join(mapa)


# Matriz de lista de adjacências 
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

def main():

    # Exemplo de início e fim, mas poderia ser qualquer outro input
    inicio = 20
    fim = 6

    grafo = Grafo(matriz_lista_adjacencia)

    caminho, distancia, direcoes = grafo.dijkstra_menor_caminho(inicio, fim)

    if distancia != float('inf'):
        print(caminho)
        print(distancia)
    else:
        print(f"Não há caminho entre {inicio} e {fim}")

    print(grafo.coordenadas_consecutivas(direcoes))

main()