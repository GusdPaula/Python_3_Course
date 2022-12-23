# LISTA DE COMPRAS

import os

lista_compras = list()

os.system('cls')

while True:

    print('\n###############################################################\n')

    condicao = input(
        'Selecione uma opção\n[i]nserir [a]pagar [l]istar [p]arar: ')
    condicao_min = condicao.lower()

    if condicao_min == 'p':
        os.system('cls')
        break

    elif condicao_min == 'i':
        os.system('cls')
        valor = input('Qual o item que deseja adicionar? ')
        lista_compras.append(valor)

    elif len(lista_compras) < 1:
        print('A lista está vazia...')
        continue

    elif condicao_min == 'a':
        while True:
            for i, v in enumerate(lista_compras):
                print(i, v)
            excluir = input('Qual o índice do item que deseja excluir?')

            try:
                del lista_compras[int(excluir)]
                break
            except ValueError:
                print('Digite um número inteiro válido...')

            except IndexError:
                print('Digite um índice que exista na lista...')

    elif condicao_min == 'l':
        for i, v in enumerate(lista_compras):
            print(i, v)

    else:
        print('Digite uma condição válida...')
