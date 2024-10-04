# Algoritmo A* (A-estrela)

## Introdução

O A* (A-estrela) é um dos algoritmos de busca mais populares e eficientes para encontrar o caminho mais curto em um grafo, sendo amplamente utilizado em áreas como Inteligência Artificial, jogos, robótica, e redes de computadores. Ele é particularmente conhecido por ser tanto completo quanto ótimo, o que significa que ele sempre encontra a solução se ela existir e garante que essa solução seja a mais curta possível.

## Como Funciona

O algoritmo A* combina características da busca de custo uniforme (que usa apenas o custo para mover de um nó para outro) e da busca heurística (que usa uma estimativa do custo restante para alcançar o objetivo). Ele faz isso usando uma função de avaliação `f(n)`:

\[
f(n) = g(n) + h(n)
\]

Onde:

- `g(n)` é o custo acumulado do caminho desde o nó inicial até o nó atual `n`.
- `h(n)` é a estimativa do custo restante para alcançar o objetivo a partir do nó `n`, chamada de função heurística.

### Passos do Algoritmo

1. **Inicialização**: O algoritmo começa adicionando o nó inicial a uma lista chamada *open list*, que contém nós a serem avaliados.
2. **Avaliação de Nós**: Ele remove o nó com o menor valor de `f(n)` da *open list* e o coloca em uma lista chamada *closed list*, que contém nós já avaliados.
3. **Expansão**: Verifica os nós vizinhos do nó atual e, para cada um, calcula seu valor de `g(n)` e `h(n)`. Se o nó não estiver na *closed list* ou se um caminho mais curto for encontrado, o nó é adicionado ou atualizado na *open list*.
4. **Finalização**: O processo continua até que o objetivo seja encontrado ou que não existam mais nós na *open list*.

### Heurísticas

A escolha da heurística `h(n)` é crucial para a eficiência do A*. As heurísticas mais comuns são:

- **Distância de Manhattan**: usada em grades onde só são permitidos movimentos ortogonais (como em labirintos).
- **Distância Euclidiana**: usada quando são permitidos movimentos diagonais.

## Aplicações

- **Jogos**: O A* é amplamente utilizado em jogos para encontrar o caminho mais curto entre pontos em um mapa.
- **Navegação**: Sistemas de navegação usam o A* para calcular rotas mais curtas entre dois pontos.
- **Robótica**: Robôs autônomos utilizam o A* para planejar caminhos em ambientes desconhecidos.

## Exemplo Visual

Se você quiser ver o algoritmo A* em ação, há várias simulações e explicações visuais que mostram como o algoritmo explora os nós até encontrar o caminho mais curto. Veja os links nas referências abaixo.

## Referências

- Playlist de explicação completa sobre o Algoritmo A*: [Guia Completo - Algoritmo A*](https://youtube.com/playlist?list=PLFt_AvWsXl0cq5Umv3pMC9SPnKjfp9eGW&si=beUcLi5corxFEdDK)
- Simulação e explicação visual: [Simulação do A*](https://www.youtube.com/watch?v=s29WpBi2exw)
- Explicação passo a passo: [A* - Explicação com exemplos](https://www.youtube.com/watch?v=BR4_SrTWbMw)

---
