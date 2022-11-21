import argparse
import mod


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--format', type=str, help='Formato do arquivo de entrada (Ex: matriz ou lista)')
    parser.add_argument(
        '--file', type=str, help='Arquivo de entrada (Ex: matriz-1.csv ou lista-1.csv)')

    args = parser.parse_args()

    if args.format == 'matriz':
        matriz = mod.read_matrix(args.file)
        print(matriz)
    elif args.format == 'lista':
        lista = mod.read_list(args.file)
        print(lista)
    else:
        print('\nEx: python3 main.py --format=matriz --file=matriz-1.csv')
        print('\nExecute \"main.py --help\" para informações de uso')


if __name__ == '__main__':
    print('Executando biblioteca do trabalho de Grafos')
    main()
