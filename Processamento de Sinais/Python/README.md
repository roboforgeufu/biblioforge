# Visualização de Dados de Sensores

Este repositório contém um script Python que lê arquivos CSV com dados de sensores de cor e os visualiza em um gráfico 3D usando Matplotlib. O script é útil para comparar visualmente as leituras de diferentes cores capturadas pelos sensores de cor do Lego Mindstorms.

## Funcionalidades

- **Importar e Converter os arquivos em CSV:** O script lê arquivos CSV e converte os dados em listas de valores para serem plotados.
- **Visualização 3D:** Os dados convertidos são usados para plotar um gráfico 3D, onde cada cor é representada por uma nuvem de pontos no espaço.
- **Comparação de Cores:** Sete cores diferentes são comparadas no gráfico, facilitando a análise das leituras dos sensores.

## Estrutura do Código

- **`import_and_convert_csv(csv_file):`** Esta função lê um arquivo CSV e retorna três listas de valores correspondentes às colunas do CSV.
- **`main():`** Esta é a função principal do script que define os eixos do gráfico, lê os arquivos CSV, e plota os dados no gráfico 3D.

## Estrutura dos Dados 

Os arquivos CSV usados no script contêm leituras de sensores para diferentes cores:

**Exemplo:**\
R, G, B\
80, 80, 84 -> leitura de sensor referente à cor branca\
80, 80, 84\
80, 80, 84\
80, 80, 84\
81, 81, 84\
80, 80, 84\
81, 80, 84\
80, 80, 84

O valor de R para a primeira leitura é igual a 80, o valor de G é igual a 80 e o valor de B é igual a 84. Dessa forma, podemos definir um ponto no espaço tridimensional: (X=R=80,Y=G=80,Z=B=84).

## Gráfico Gerado
![image](https://github.com/user-attachments/assets/cc2cc7dc-78d3-45b4-9bbf-6e87046e345d)
