import argparse

import mod
from graph_processor import GraphProcessor


def main():
    parser = argparse.ArgumentParser(
        prog='main.py',
        epilog='Ex: python main.py --format=matriz --file=data/matriz-1.csv --operation=criacao_arestas --extra_args=2'
    )

    parser.add_argument('--format', type=str, help='Formato do arquivo de entrada', choices=['matriz', 'lista'], required=True)
    parser.add_argument('--file', type=str, help='Arquivo de entrada (Ex: data/matriz-1.csv ou data/lista-1.csv)', required=True)
    parser.add_argument('--operation', type=str, help='Operacao a ser realizada (Ex: ponderacao_vertices)', required=True)
    parser.add_argument('--extra_args', type=str, help='[Opcional] Argumentos extras, veja README.md para documentacao completa '
                                                       '(Ex: extra_args=3)',  required=False)

    args = parser.parse_args()

    if args.format == 'matriz':
        print('Processando MATRIZ de adjacencias')
    elif args.format == 'lista':
        print('Processando LISTA de adjacencias')
    else:
        parser.print_help()

    matriz = mod.read(args.file)

    graph_processor = GraphProcessor(args.format, matriz)

    if args.operation == 'criacao_grafo_x_vertices':
        graph_processor.criacao_grafo_x_vertices(args.extra_args)


if __name__ == '__main__':
    print('Trabalho de teoria de grafos e computabilidade (Eng Software / PUC Minas)')
    print('Aluno: Leonardo Gianluca')
    print('')

    main()
