"""
Simulação de um grafo representando um mapa com nós de interseção, plataformas e pontos de coleta de cubos. 

O grafo suporta:
    - Adição e remoção de arestas
    - Marcação e desmarcação de obstáculos
    - Exibição da matriz de adjacência e informações dos nós
"""

from enum import Enum
import heapq
import time

# ENUMS ---------------------

class NodeType(Enum):
    '''Enum para tipo de nó (INTERSECTION, PLATFORM, CUBE_COLLECTION)'''
    INTERSECTION = 1
    PLATFORM = 2
    CUBE_COLLECTION = 3
    OBSTACLE = 4 


class CubeStatus(Enum):
    '''Enum para status de cubo (UNKNOWN, PRESENT, ABSENT)'''
    UNKNOWN = 0 # não sabemos se há cubo
    DETECTED = 1
    COLLECTED = 2
    ABSENT = 3 # nao tem cubo

# NÓ ------------------------

class Node:

    ''' 
        Representa um nó do grafo
        Para mapenamento dos nós por vista, usei time.time
        Não sei se é o jeito mais eficaz de guarda essa informação. Poderia usar int e ir incrementando cada vez que o robô passa no nó também'''

    def __init__(self, id, name, node_type=NodeType.INTERSECTION):
        self.id = id
        self.name = name
        self.node_type = node_type
        self.cube_status = CubeStatus.UNKNOWN # o status é iniciado como unkniwn
        self.cube_color = None # cor do cubo identificado no ponto de coleta
        self.platform_color = None # cor da plataforma (se node_type == PLATFORM). Talvez seria legal criar um enum pra cor também
        self.cubes_delivered = 0  # contador de cubos entregues na plataforma
        self.last_visit_time = None # timestamp da última visita do robô

    def visit(self):
        '''Atualiza variavel que guarda o tempo da última visita'''
        self.last_visit_time = time.time()

    # função que imprime o nó: 
    def __repr__(self):
        return (f"Node(id={self.id}, name={self.name}, "
                f"type={self.node_type.name}, "
                f"cube_status={self.cube_status.name}, cube_color={self.cube_color}, "
                f"platform_color={self.platform_color}, cubes_delivered={self.cubes_delivered}, "
                f"last_visit_time={self.last_visit_time})")


# GRAFO -----------------

class Grafo:
    def __init__(self, num_nos):
        self.num_nodes = num_nos
        self.map_matrix = [[] for _ in range(num_nos)] #lista de lista, cada nó é uma lisra de adjacencia
        self.nodes = [Node(i, f"N{i}") for i in range(num_nos)] #cria nodes para dada lista dentro da lista grafo
        self.obstacles = set()  # ids de nós que representam áreas inacessíveis, inicialmente vazio

    def adicionar_arestas(self, origem, destino, direcao, peso=1):
        if origem in self.obstacles or destino in self.obstacles:
            return
        self.map_matrix[origem].append([origem, destino, direcao, peso])
        # armazenando direção oposta:
        direcao_inversa = {
            "N": "S", "S": "N", "L": "O", "O": "L", "P": "P"
        }[direcao]
        self.map_matrix[destino].append([destino, origem, direcao_inversa, peso])

    def remove_edge(self, origin, destination):
        self.map_matrix[origin] = [e for e in self.map_matrix[origin] if e[1] != destination] # mantem arestas que não são destination
        self.map_matrix[destination] = [e for e in self.map_matrix[destination] if e[1] != origin] 

    def mark_obstacle(self, origin, destination):
        """Marca uma aresta como inacessível temporariamente.Para isso, muda seu peso para infinito. Mesma coisa do ano passado"""
        for edge in self.map_matrix[origin]:
            if edge[1] == destination:
                edge[3] = float("inf")
        for edge in self.map_matrix[destination]:
            if edge[1] == origin:
                edge[3] = float("inf")

    def unmark_obstacle(self, origin, destination, weight=1):
        """Remove marcação de obstáculo, restaurando peso da aresta."""
        for edge in self.map_matrix[origin]:
            if edge[1] == destination:
                edge[3] = weight
        for edge in self.map_matrix[destination]:
            if edge[1] == origin:
                edge[3] = weight

    def set_fixed_obstacle(self, node_id):
        """Marca nó como área inascessivel.
        Muda tipo do nó pra obstaculo 
        Adiciona nó na lista de obstaculos"""
        self.nodes[node_id].node_type = NodeType.OBSTACLE
        self.obstacles.add(node_id)
    
    def dijkstra(self, start, end):
        '''
        Calcula caminho mínimo considerando obstáculos fixos e temporários.
        Retorna lista de (node, direcao) para execução do robô.
        '''
        distances = {node.id: float("inf") for node in self.nodes} # guarda menor custo de nó inicio até nó v
        previous = {node.id: None for node in self.nodes} # guarda o nó anterior no caminho mais curto até v
        prev_dir = {node.id: None for node in self.nodes}  # guarda a direção usada

        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_dist, current_node = heapq.heappop(queue)
            if current_dist > distances[current_node]:
                continue
            if current_node == end:
                break
            for edge in self.map_matrix[current_node]:
                _, neighbor, direcao, weight = edge
                # ignora se for obstáculo
                if weight == float("inf") or self.nodes[neighbor].node_type == NodeType.OBSTACLE:
                    continue
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    prev_dir[neighbor] = direcao
                    heapq.heappush(queue, (new_dist, neighbor))

        # reconstrói caminho
        if distances[end] == float("inf"):
            return None  # não existe caminho

        path = []
        node = end
        while node is not None:
            path.insert(0, (node, prev_dir[node]))
            node = previous[node]

        # o primeiro nó (start) não tem direção de entrada → tira o None
        if path and path[0][1] is None:
            path[0] = (path[0][0], "START")

        return path


    def show_matrix(self):
        '''MOstra matriz associada ao grafo'''
        print("\n=== MAP MATRIX ===")
        for i, edges in enumerate(self.map_matrix):
            print(f"Node {i}: {edges}")

    def show_nodes_info(self):
        '''Mostra informações associadas a cada nó. É mais ampla que show_matriz'''
        print("\n=== NODES INFO ===")
        for node in self.nodes:
            print(node)


# INICIALIZAÇÃO DO MAPA ------------------------------------

# Conexões horizontais
HORIZONTAL_EDGES = [
    (0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),
    (18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(24,25),(25,26),(26,27),(27,28),(28,29),
    (36,37),(37,38),(38,39),(39,40),(40,41),(41,42),(42,43),(43,44),(44,45),(45,46),(46,47),
    (54,55),(55,56),(56,57),(57,58),(58,59),(59,60),(60,61),(61,62),(62,63),(63,64),(64,65),
    (72,73),(73,74),(74,75),(75,76),(76,77),(77,78),(78,79),(79,80),(80,81),(81,82),(82,83)
]

# Conexões verticais
VERTICAL_EDGES = [
    (0,12),(2,13),(4,14),(6,15),(8,16),(10,17),(11,29),
    (12,18),(13,20),(14,22),(15,24),(16,26),(17,28),
    (18,30),(20,31),(22,32),(24,33),(26,34),(28,35),(29,47),
    (30,36),(31,38),(32,40),(33,42),(34,44),(35,46),
    (36,48),(38,49),(40,50),(42,51),(44,52),(46,53),(47,65),
    (48,54),(49,56),(50,58),(51,60),(52,62),(53,64),
    (54,66),(56,67),(58,68),(60,69),(62,70),(64,71),(65,83),
    (66,72),(67,74),(68,76),(69,78),(70,80),(71,82)
]


def initialize_map_structure(grafo):
    """Inicializa o mapa de nós, interseções, cubos e plataformas."""

    # horizontais
    for n1, n2 in HORIZONTAL_EDGES:
        direcao = calcular_direcao(n1, n2)
        grafo.adicionar_arestas(n1, n2, direcao, 1)

    # verticais
    for n1, n2 in VERTICAL_EDGES:
        direcao = calcular_direcao(n1, n2)
        grafo.adicionar_arestas(n1, n2, direcao, 1)

    # plataformas
    platform_nodes = [84, 85, 86, 87, 88]
    entrada_crossings = [11, 29, 47, 65, 83]  # cruzamentos conectados às plataformas
    for cross, platform in zip(entrada_crossings, platform_nodes):
        grafo.adicionar_arestas(cross, platform, "P", 2)  # usa "P" em vez de "L"
        grafo.nodes[platform].node_type = NodeType.PLATFORM
        grafo.nodes[platform].platform_color = None

    # pontos de coleta de cubos
    cube_nodes = [
        1,  3,  5,  7,  9,
        12, 13, 14, 15, 16, 17,
        19, 21, 23, 25, 27,
        30, 31, 32, 33, 34, 35,
        37, 39, 41, 43, 45,
        48, 49, 50, 51, 52, 53,
        55, 57, 59, 61, 63,
        66, 67, 68, 69, 70, 71,
        73, 75, 77, 79, 81
    ]
    for n in cube_nodes:
        grafo.nodes[n].node_type = NodeType.CUBE_COLLECTION
        grafo.nodes[n].cube_status = CubeStatus.UNKNOWN

def calcular_direcao(origem, destino):
    """Calcula direção baseada nas conexões reais do mapa"""

    # horizontais
    if (origem, destino) in HORIZONTAL_EDGES:
        return "L"
    if (destino, origem) in HORIZONTAL_EDGES:
        return "O"

    # verticais
    if (origem, destino) in VERTICAL_EDGES:
        return "S"
    if (destino, origem) in VERTICAL_EDGES:
        return "N"

    return "P"  # plataformas


# TESTE ------------------------------------------
if __name__ == "__main__":
    g = Grafo(89)
    initialize_map_structure(g)
    g.show_matrix()

    # informações detalhadas dos nós
    #g.show_nodes_info()

    # TESTE 1: Caminho simples
    print("\n TESTE 1: Caminho simples (0 -> 11)")
    path = g.dijkstra(0, 11)
    if path:
        print(f"Caminho encontrado com {len(path)} passos:")
        for i, (node, direction) in enumerate(path):
            print(f"   {i+1}. Nó {node} -> {direction}")
    else:
        print("Caminho não encontrado")

    # TESTE 2: Caminho até plataforma
    print("\nTESTE 2: Caminho até plataforma (0 -> 84)")
    path_platform = g.dijkstra(0, 84)
    if path_platform:
        nodes = [node for node, _ in path_platform]
        print(f"Caminho encontrado: {nodes}")
        print(f" Passa pelo nó 11: {'Sim' if 11 in nodes else 'Nao'}")
    else:
        print("Caminho não encontrado")

    # TESTE 3: Bloqueio de aresta
    print("\nTESTE 3: Bloqueando aresta 5-6")
    path_before = g.dijkstra(0, 11)
    len_before = len(path_before) if path_before else 0
    
    g.mark_obstacle(5, 6)  # Bloqueia aresta
    path_after = g.dijkstra(0, 11)
    len_after = len(path_after) if path_after else 0
    
    print(f"   Antes do bloqueio: {len_before} passos")
    print(f"   Depois do bloqueio: {len_after} passos")
    
    if path_after:
        nodes = [node for node, _ in path_after]
        if 5 in nodes and 6 in nodes:
            print("ERRO: Ainda passa por 5-6!")
        else:
            print("Deu certo uhuu. Contornou obstáculo corretamente")
    
    # TESTE 4: Removendo bloqueio
    print("\nTESTE 4: Removendo bloqueio da aresta 5-6")
    g.unmark_obstacle(5, 6)
    path_restored = g.dijkstra(0, 11)
    len_restored = len(path_restored) if path_restored else 0
    
    print(f"   Caminho restaurado: {len_restored} passos")
    print(f"   Mesmo tamanho original: {'SIm' if len_restored == len_before else 'Não'}")

    # TESTE 5: Obstáculo fixo
    print("\nTESTE 5: Marcando nó 1 como obstáculo fixo")
    path_normal = g.dijkstra(0, 13)
    if path_normal:
        nodes_normal = [node for node, _ in path_normal]
        print(f"   Caminho normal (0->13): {nodes_normal}")
    
    g.set_fixed_obstacle(1)
    path_blocked = g.dijkstra(0, 13)
    
    if path_blocked:
        nodes_blocked = [node for node, _ in path_blocked]
        print(f"   Caminho com obstáculo: {nodes_blocked}")
        if 1 in nodes_blocked:
            print("ERRO")
        else:
            print("Evitou nó obstáculo corretamente")
    else:
        print("Nenhum caminho alternativo encontrado")

    # TESTE 6: Cenário impossível
    print("\nTESTE 6: Bloqueando acesso à plataforma")
    g2 = Grafo(89)
    initialize_map_structure(g2)
    g2.mark_obstacle(11, 84)  # Bloqueia única conexão para plataforma 84
    
    impossible_path = g2.dijkstra(0, 84)
    if impossible_path is None:
        print("Corretamente detectou caminho impossível")
    else:
        print("ERRO: Encontrou caminho quando não deveria")

    print()
    print(g.nodes[2])
    print(g.nodes[84])

    # simula visita do robô em alguns nós
    g.nodes[2].visit()
    g.nodes[84].visit()
    print("\nNós 2 e 84 após visita do robô:")
    print()
    print(g.nodes[2])
    print(g.nodes[84])