### Calculator ###

conta = 0

while True:
    conta = 0
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operacao = input('Digite o operador: (+, -, /, *) ')

    try:
        int_numero_1, int_numero_2 = int(numero_1), int(numero_2)

        if operacao == '+':
            conta = int_numero_1 + int_numero_2

        elif operacao == '-':
            conta = int_numero_1 - int_numero_2

        elif operacao == '/':
            conta = int_numero_1 / int_numero_2

        elif operacao == '*':
            conta = int_numero_1 * int_numero_2

        else:
            print('Por favor, siga as instruções.')
            continue

        print(f'O resultado da conta {int_numero_1} {operacao} {int_numero_2} é {conta}.')

        condi_sair = input('Quer continuar? S/N  ')

        if condi_sair.upper() == 'S':
            break

    except Exception as error:
        print(error)

print('Você saiu.')