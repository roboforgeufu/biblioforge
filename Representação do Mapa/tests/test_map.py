import pytest
from map import Grafo, NodeType, CubeStatus, calcular_direcao, initialize_map_structure

@pytest.fixture
def mapa():
    g = Grafo(89)
    initialize_map_structure(g)  # Função externa, não método da classe
    return g


def find_edge(graph: Grafo, origin: int, destination: int):
    """Encontra uma aresta específica na matriz de adjacência"""
    for e in graph.map_matrix[origin]:
        if e[1] == destination:
            return e
    return None


def test_total_nodes_and_types(mapa):
    """Testa se o número total de nós e tipos estão corretos"""
    assert mapa.num_nodes == 89

    # Testa plataformas
    plataformas = [84, 85, 86, 87, 88]
    for p in plataformas:
        assert mapa.nodes[p].node_type == NodeType.PLATFORM
        assert mapa.nodes[p].platform_color is None

    # Testa alguns pontos de coleta específicos
    pontos_coleta_sample = [1, 3, 5, 7, 9, 13, 25, 37, 49, 67, 79]
    for n in pontos_coleta_sample:
        assert mapa.nodes[n].node_type == NodeType.CUBE_COLLECTION
        assert mapa.nodes[n].cube_status == CubeStatus.UNKNOWN


def test_crossings_to_platforms(mapa):
    """Testa conexões entre cruzamentos e plataformas"""
    cruzamentos = [11, 29, 47, 65, 83]
    plataformas = [84, 85, 86, 87, 88]

    for c, p in zip(cruzamentos, plataformas):
        # Testa aresta cruzamento -> plataforma
        e = find_edge(mapa, c, p)
        assert e is not None, f"Aresta {c} -> {p} não encontrada"
        assert e[2] == "P", f"Direção esperada 'P', encontrada '{e[2]}'"
        assert e[3] == 2, f"Peso esperado 2, encontrado {e[3]}"
        
        # Testa aresta de volta plataforma -> cruzamento
        rev = find_edge(mapa, p, c)
        assert rev is not None, f"Aresta de volta {p} -> {c} não encontrada"
        assert rev[2] == "P", f"Direção de volta esperada 'P', encontrada '{rev[2]}'"


def test_horizontal_and_vertical_edges(mapa):
    """Testa arestas horizontais e verticais básicas"""
    # Horizontal simples: 0 → 1
    e01 = find_edge(mapa, 0, 1)
    assert e01 is not None, "Aresta 0 -> 1 não encontrada"
    assert e01[2] == "L", f"Direção esperada 'L', encontrada '{e01[2]}'"

    # Vertical simples: 0 → 12
    e012 = find_edge(mapa, 0, 12)
    assert e012 is not None, "Aresta 0 -> 12 não encontrada"
    assert e012[2] == "S", f"Direção esperada 'S', encontrada '{e012[2]}'"

    # Testa direções inversas
    e10 = find_edge(mapa, 1, 0)
    assert e10 is not None and e10[2] == "O", "Direção inversa 1 -> 0 incorreta"
    
    e120 = find_edge(mapa, 12, 0)
    assert e120 is not None and e120[2] == "N", "Direção inversa 12 -> 0 incorreta"


def test_dijkstra_basic_path_in_map(mapa):
    """Testa caminho básico usando Dijkstra"""
    # Caminho de 0 até 11 (linha superior até cruzamento)
    path = mapa.dijkstra(0, 11)
    assert path is not None, "Caminho 0 -> 11 não encontrado"
    
    nodes = [n for n, _ in path]
    
    # Deve começar em 0 e terminar em 11
    assert nodes[0] == 0, f"Nó inicial esperado 0, encontrado {nodes[0]}"
    assert nodes[-1] == 11, f"Nó final esperado 11, encontrado {nodes[-1]}"
    
    # Deve conter todos os nós de 0 até 11 (caminho direto horizontal)
    expected_nodes = list(range(12))  # 0..11
    assert all(i in nodes for i in expected_nodes), f"Caminho não contém todos os nós esperados: {expected_nodes}"

    # Testa se as direções estão corretas
    for i in range(len(path) - 1):
        current_node, _ = path[i]
        next_node, next_direction = path[i + 1]
        expected_direction = calcular_direcao(current_node, next_node)
        assert next_direction == expected_direction, \
            f"Direção incorreta de {current_node} -> {next_node}: esperado {expected_direction}, encontrado {next_direction}"


def test_dijkstra_platform_path(mapa):
    """Testa caminho até plataforma"""
    # Caminho até plataforma conectada ao nó 11
    path = mapa.dijkstra(0, 84)
    assert path is not None, "Caminho 0 -> 84 não encontrado"
    
    nodes = [n for n, _ in path]
    assert nodes[0] == 0, f"Nó inicial esperado 0, encontrado {nodes[0]}"
    assert nodes[-1] == 84, f"Nó final esperado 84, encontrado {nodes[-1]}"
    
    # Deve passar pelo cruzamento 11
    assert 11 in nodes, "Caminho não passa pelo cruzamento 11"


def test_blocked_edge_breaks_path(mapa):
    """Testa se bloqueio de aresta interrompe caminho"""
    # Caminho normal deve existir
    path1 = mapa.dijkstra(0, 84)
    assert path1 is not None, "Caminho normal 0 -> 84 não encontrado"

    # Bloqueia aresta final 11-84
    mapa.mark_obstacle(11, 84)
    
    # Agora o caminho deve ser impossível
    path2 = mapa.dijkstra(0, 84)
    assert path2 is None, "Caminho ainda existe após bloqueio da única conexão"


def test_obstacle_detour(mapa):
    """Testa se algoritmo consegue contornar obstáculos"""
    # Caminho normal
    path_normal = mapa.dijkstra(0, 11)
    assert path_normal is not None
    len_normal = len(path_normal)
    
    # Bloqueia uma aresta no meio do caminho
    mapa.mark_obstacle(5, 6)
    
    # Deve encontrar caminho alternativo
    path_detour = mapa.dijkstra(0, 11)
    assert path_detour is not None, "Não encontrou caminho alternativo"
    
    # Caminho alternativo deve ser mais longo
    assert len(path_detour) > len_normal, "Caminho alternativo não é mais longo que o original"
    
    # Não deve passar pelos nós bloqueados
    nodes_detour = [n for n, _ in path_detour]
    consecutive_5_6 = any(nodes_detour[i] == 5 and nodes_detour[i+1] == 6 
                         for i in range(len(nodes_detour)-1))
    consecutive_6_5 = any(nodes_detour[i] == 6 and nodes_detour[i+1] == 5 
                         for i in range(len(nodes_detour)-1))
    
    assert not consecutive_5_6 and not consecutive_6_5, "Caminho ainda passa pela aresta bloqueada"


def test_fixed_obstacle_node(mapa):
    """Testa nó marcado como obstáculo fixo"""
    # Caminho normal passando pelo nó 1
    path_normal = mapa.dijkstra(0, 2)
    assert path_normal is not None
    nodes_normal = [n for n, _ in path_normal]
    
    # Marca nó 1 como obstáculo fixo
    mapa.set_fixed_obstacle(1)
    
    # Verifica se nó foi marcado corretamente
    assert mapa.nodes[1].node_type == NodeType.OBSTACLE
    assert 1 in mapa.obstacles
    
    path_blocked = mapa.dijkstra(0, 2)
    
    if path_blocked:  # Se existe caminho alternativo
        nodes_blocked = [n for n, _ in path_blocked]
        assert 1 not in nodes_blocked, "Caminho passa pelo nó marcado como obstáculo"
    # Se não existe caminho alternativo, isso também é válido


def test_node_visit_functionality(mapa):
    """Testa funcionalidade de visita a nós"""
    node = mapa.nodes[0]
    
    assert node.last_visit_time is None
    
    node.visit()
    assert node.last_visit_time is not None
    
    first_visit = node.last_visit_time
    import time
    time.sleep(0.001)  # Pequena pausa para garantir timestamp diferente
    node.visit()
    assert node.last_visit_time > first_visit


def test_cube_status_initialization(mapa):
    """Testa inicialização correta dos status de cubos"""
    # Pontos de coleta devem começar com status UNKNOWN
    cube_nodes = [1, 3, 5, 7, 9, 13, 19, 25, 37, 49, 67, 79]
    
    for node_id in cube_nodes:
        node = mapa.nodes[node_id]
        assert node.node_type == NodeType.CUBE_COLLECTION
        assert node.cube_status == CubeStatus.UNKNOWN
        assert node.cube_color is None
        
    platform_nodes = [84, 85, 86, 87, 88]
    for node_id in platform_nodes:
        node = mapa.nodes[node_id]
        assert node.node_type == NodeType.PLATFORM
        assert node.cubes_delivered == 0