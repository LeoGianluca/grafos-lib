# Trabalho de grafos

## Introducão

Este é o trabalho de grafos

## Utilização

A aplicação apresentada no trabalho foi desenvolvida em Python e abaixo seguem instruções de uso

OBS: Antes de executar verificar a existencia do alias 'python' apontando para uma instalação válida de Python 3, caso não exista 
substituir a palavra 'python' por 'python3' em sistemas baseados em UNIX (Ex: Linux e MacOS)

```bash
Cenário 1 - Criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)

python main.py --format=matriz --file-out=data/out/criacao-grafo-x-vertices-1.csv --operation=criacao_grafo_x_vertices --extra_args=7

'extra_args' = Número de arestas do grafo a ser gerado
```

```bash
Cenário 2 - Criação e remoção de arestas

python main.py --format=matriz --file-in=data/in/teste-matriz-1.csv --file-out=data/out/matriz-criacao_arestas-output.csv --operation=criacao_arestas --extra_args=2
python main.py --format=matriz --file=data/teste-lista-1.csv --operation=remocao_arestas --extra_args=3

'extra_args' = Número de arestas adicionadas ou removidas no grafo
```

```bash
Cenário 3 - Ponderação e rotulação de vértices

python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=ponderacao_vertices
python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=rotulacao_vertices
```

```bash
Cenário 4 - Ponderação e rotulação de arestas

python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=ponderacao_arestas
python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=rotulacao_arestas
```

```bash
Cenário 4 - Checagem de adjacência entre vértices

python main.py --format=matriz --file=data/teste-matriz-1.csv --file-out=data/out/checagem_adjacencia_vertices-output.txt 
--operation=checagem_adjacencia_vertices
```

```bash
Cenário 5 - Checagem de adjacência entre arestas

python3 main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_adjacencia_arestas
```

```bash
Cenário 6 - Checagem de existência de arestas

python3 main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_adjacencia_arestas
```

```bash
Cenário 7 - Checagem da quantidade de vértices e arestas

python3 main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_quantidade_vertices
python3 main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_quantidade_arestas
```

```bash
Cenário 8 - Checagem de grafo vazio e completo

python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_grafo_vazio
python main.py --format=matriz --file=data/teste-matriz-1.csv --operation=checagem_grafo_completo
```
