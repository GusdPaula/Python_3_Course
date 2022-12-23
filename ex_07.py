# VALIDADOR DE CPF
import re

while True:
    cpf = input('Digite o CPF com pontos e traços:\nEx.: xxx.xxx.xxx-xx \n')

    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) is not 11:
        print('Acho que digitou valores insuficientes ou mais que o necessário.')

    elif (len(cpf) * cpf[0]) == cpf:
        print('Números repetidos não são válidos...')

    else:
        break

# Verificando o primeiro dígito
mult_dez = 10
soma = 0
i = 9

for v in cpf:
    if i == 0:
        break
    elif v not in '-.':
        soma += (int(v) * mult_dez)
        mult_dez -= 1
        i -= 1

mult_total = soma * 10
resto = mult_total % 11
dig_1 = 0 if resto > 9 else resto

print('\n##########################\n')

if str(dig_1) == cpf[-2]:
    print(f'Primeiro dígito {dig_1} ok!')
else:
    print(f'O primeiro dígito deveria ser {cpf[-2]}, não {dig_1}')

print('\n##########################\n')

# Verificando o segundo dígito
mult_dez_2 = 11
soma_2 = 0
i_2 = 10

for v in cpf:
    if i_2 == 0:
        break
    elif v not in '-.':
        soma_2 += (int(v) * mult_dez_2)
        mult_dez_2 -= 1
        i_2 -= 1

mult_total_2 = soma_2 * 10
resto_2 = mult_total_2 % 11
dig_2 = 0 if resto_2 > 9 else resto_2

if str(dig_2) == cpf[-1]:
    print(f'Segundo dígito {dig_2} ok!')
else:
    print(f'O segundo dígito deveria ser {cpf[-1]}, não {dig_2}')

print('\n##########################\n')

# Verificando o CPF no geral
if str(dig_1) == cpf[-2] and str(dig_2) == cpf[-1]:
    print('O CPF é válido.')

else:
    print('CPF inválido...')

print('\n##########################\n')
