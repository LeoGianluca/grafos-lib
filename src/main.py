import argparse

import file_processor
from graph_processor import GraphProcessor


def main():
    parser = argparse.ArgumentParser(
        prog='main.py',
        epilog='Ex: python main.py --format=matriz --file=data/matriz-1.csv --operation=criacao_arestas --extra_args=2'
    )

    parser.add_argument('--format', type=str, help='Formato do arquivo de entrada', choices=['matriz', 'lista'],
                        required=True)
    parser.add_argument('--file', type=str, help='Arquivo de entrada (Ex: data/matriz-1.csv ou data/lista-1.csv)',
                        required=True)
    parser.add_argument('--operation', type=str, help='Operacao a ser realizada (Ex: ponderacao_vertices)',
                        required=True)
    parser.add_argument('--extra_args', type=str,
                        help='[Opcional] Argumentos extras, veja README.md para documentacao completa '
                             '(Ex: extra_args=3)', required=False)

    args = parser.parse_args()

    graph_info = file_processor.read(args.file, args.format)

    graph_processor = GraphProcessor(args.format, graph_info)

    # Dicionário de mapeamento do parametro de entrada (--operation) para o método de processamento correspondente
    # para métodos com 1 argumento adicional
    functions_extra_args = {
        'criacao_grafo_x_vertices': graph_processor.criacao_grafo_x_vertices,
        'criacao_arestas': graph_processor.criacao_arestas,
        'remocao_arestas': graph_processor.remocao_arestas,
        'checagem_adjacencia_vertices': graph_processor.checagem_adjacencia_vertices,
        'checagem_adjacencia_arestas': graph_processor.checagem_adjacencia_arestas,
        'checagem_existencia_arestas': graph_processor.checagem_existencia_arestas,
    }

    # Dicionário de mapeamento do parametro de entrada (--operation) para o método de processamento correspondente
    # para métodos sem argumentos
    functions_no_extra_args = {
        'ponderacao_vertices': graph_processor.ponderacao_vertices,
        'rotulacao_vertices': graph_processor.rotulacao_vertices,
        'ponderacao_arestas': graph_processor.ponderacao_arestas,
        'rotulacao_arestas': graph_processor.rotulacao_arestas,
        'checagem_quantidade_vertices': graph_processor.checagem_quantidade_vertices,
        'checagem_quantidade_arestas': graph_processor.checagem_quantidade_arestas,
        'checagem_grafo_vazio': graph_processor.checagem_grafo_vazio,
        'checagem_grafo_completo': graph_processor.checagem_grafo_completo,
    }

    # Nome da operação informada na chamada do programa (Ex: --operation=rotulacao_vertices)
    func_name = args.operation

    print(f"Localizando operação '{func_name}'")
    print("")

    # Verificando a lista de funções e executando o método, caso localizado
    if func_name in functions_extra_args:
        functions_extra_args[func_name](args.extra_args)
    elif func_name in functions_no_extra_args:
        functions_no_extra_args[func_name]()
    else:
        print("Operação não localizada, verifique a documentação")


if __name__ == '__main__':
    print('')
    print('Trabalho de teoria de grafos e computabilidade (Eng Software / PUC Minas)')
    print('Aluno: Leonardo Gianluca')
    print('')

    main()
