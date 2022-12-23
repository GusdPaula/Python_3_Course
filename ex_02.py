################################ Ex 01 ######################################################

'''
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')

except:
    print(f'O número {numero} não é inteiro.')
'''

################################ Ex 02 ######################################################

'''
hora_atual = input('Qual o horário agora? Ex.: 14:11   ')

try:
    hora = int(hora_atual[0:2])
    if hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde')
    else:
        print('Boa noite!')

except:
    print('Por favor, siga o exemplo.')
'''

################################ Ex 03 ######################################################

'''
nome = input('Qual o seu primeiro nome:  ')

try:
    med_nome = len(nome)

    if med_nome <= 4:
        print('Seu nome é curto.')
    elif med_nome <= 6:
        print('Seu nome é nomral.')
    else:
        print('Seu nome é muito grande.')

except:
    print('Digite um nome válido.')
'''