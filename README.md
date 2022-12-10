# Trabalho de grafos

## Introducão

Este é o trabalho de grafos

## Utilização

A aplicação apresentada no trabalho foi desenvolvida em Python e abaixo seguem instruções de uso

OBS 1: Antes de executar verificar a existencia do alias 'python' apontando para uma instalação válida de Python 3, caso não exista 
substituir a palavra 'python' por 'python3' em sistemas baseados em UNIX (Ex: Linux e MacOS)

OBS 2: Os comandos abaixo estão configurados para execução na pasta raiz da aplicação, no mesmo nível deste arquivo (README.md)

```bash
Cenário 1 - Criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)

python ./src/main.py --format=matriz --file-out=./src/data/out/output1-criacao-grafo-x-vertices-output.csv --operation=criacao_grafo_x_vertices --extra_args=7

Onde 'extra_args' = Número de arestas do grafo a ser gerado
```

```bash
Cenário 2 - Criação e remoção de arestas

python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output2-criacao-arestas.csv --operation=criacao_arestas --extra_args=2
python ./src/main.py --format=lista --file-in=./src/data/in/teste-lista-1.csv --file-out=./src/data/out/output3-remocao-arestas-output.csv --operation=remocao_arestas --extra_args=3

Onde 'extra_args' = Número de arestas adicionadas ou removidas no grafo
```

```bash
Cenário 3 - Ponderação e rotulação de vértices

python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output4-ponderacao-vertices-output.csv --operation=ponderacao_vertices
python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output5-rotulacao-vertices-output.csv --operation=rotulacao_vertices
```

```bash
Cenário 4 - Ponderação e rotulação de arestas

python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output6-rotulacao-vertices-output.csv --operation=ponderacao_arestas
python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output7-rotulacao-vertices-output.csv --operation=rotulacao_arestas
```

```bash
Cenário 4 - Checagem de adjacência entre vértices

python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output8-checagem-adjacencia-vertices-output.txt --operation=checagem_adjacencia_vertices
```

```bash
Cenário 5 - Checagem de adjacência entre arestas

python3 ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output9-checagem-adjacencia-arestas-output.txt  --operation=checagem_adjacencia_arestas
```

```bash
Cenário 6 - Checagem de existência de arestas

python3 ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output10-checagem-existencia-arestas-output.txt --operation=checagem_existencia_arestas
```

```bash
Cenário 7 - Checagem da quantidade de vértices e arestas

python3 ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output11-checagem-quantidade-vertices-output.txt --operation=checagem_quantidade_vertices
python3 ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output12-checagem-quantidade-arestas-output.txt --operation=checagem_quantidade_arestas
```

```bash
Cenário 8 - Checagem de grafo vazio e completo

python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output13-checagem-grafo-vazio-output.txt --operation=checagem_grafo_vazio
python ./src/main.py --format=matriz --file-in=./src/data/in/teste-matriz-1.csv --file-out=./src/data/out/output14-checagem-grafo-completo-output.txt --operation=checagem_grafo_completo
```
