from queue import PriorityQueue
from pyamaze import maze, agent, COLOR
import time


def h_score(celula, destino):
    linha_c = celula[0]
    coluna_c = celula[1]
    linha_d = destino[0]
    coluna_d = destino[1]

    return abs(coluna_d - coluna_c) + abs(linha_d - linha_c)


def aestrela(labirinto):
    comecou = time.time()
    print('Calculando...')
    # destino
    destino = (1, 1)

    # iniciar todo mundo infinito
    f_score = {celula: float('inf') for celula in labirinto.grid}
    g_score = {}

    # calcular celula inicial
    celula_inicial = (labirinto.rows, labirinto.cols)
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    # iniciar fila de prioridade com f da celula inicial, h da celula inicial, e a celula inicial
    fila = PriorityQueue()
    fila.put((f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial))

    caminho = {}
    # enquanto tiver elementos na fila
    while not fila.empty():
        # pega o primeiro item da fila de prioridade
        celula = fila.get()[2]

        # se a celula atual é o destino, acabou!
        if celula == destino:
            break

        # verifica quais os vizinhos possiveis
        for direcao in 'NSEW':
            if labirinto.maze_map[celula][direcao]:
                if direcao == 'N':
                    proxima_celula = (celula[0] - 1 , celula[1])
                elif direcao == 'S':
                    proxima_celula = (celula[0] + 1 , celula[1])
                elif direcao == 'E':
                    proxima_celula = (celula[0], celula[1] + 1)
                else:
                    proxima_celula = (celula[0], celula[1] - 1)

                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)

                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    fila.put((novo_f_score, h_score(proxima_celula, destino), proxima_celula))
                    caminho[proxima_celula] = celula

    caminho_final = {}
    celula_analisada = destino

    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]

    acabou = time.time() - comecou
    print(f'{acabou:.4f}s calculando caminho')
    return caminho_final


inicio = time.time()
labirinto = maze(100, 100)
labirinto.CreateMaze(loopPercent=30)
print(f'{(time.time() - inicio):.4f}s criando labirinto')

agent_1 = agent(labirinto, filled=True, footprints=True, color=COLOR.blue)
caminho = aestrela(labirinto)

labirinto.tracePath({agent_1: caminho}, delay=5)
labirinto.run()