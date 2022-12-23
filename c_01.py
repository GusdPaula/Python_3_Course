print('Hello, world!')

# The print function broke the line and add a space after non-named arguments
print(12, 43)

# But we can change the delimiter using 'sep='
print(12, 34, sep="-")

# We can change the end of the print too
print(12, 34, sep="-", end='##\n')

# Read PEP8

# '...' can be used an ellipse, it won't cause error.
ip = ...

# String formatting
name = 'Gustavo'
height = 1.80

line_1 = f'{name} has {height:.3f}'  # Here we can change the zeros after dot

print(line_1)

height = 100000.80

line_1 = f'{name} has {height:,.3f}'  # Here we can put a comma to delimiter

print(line_1)

a = 'A'
b = 'B'
c = 1.1

formatting = 'a={}, b={}, c={}'.format(a, b, c)

print(formatting)

formatting = 'b={1}, a={0}, c={2}'.format(a, b, c)

print(formatting)

formatting = 'b={t2}, a={t1}, c={t3}'.format(t1=a, t2=b, t3=c)

print(formatting)

# Boolean
print(10 > 12)  # Return a False value
print(13 > 12)  # Return a True value

# Interpolação básica de string
'''
s - string
d & i - int
f - float
x & X - Hexadecimal
'''

nome = 'Luiz'
preco = 1000.9474734334
variavel = '%s o preço é R$%f' % (nome, preco)
print(variavel)

nome = 'Luiz'
preco = 1000.9474734334
variavel = '%s o preço é R$%.2f' % (nome, preco)
print(variavel)

print('o hexadecimal de %d é %x' % (15, 15))
print('o hexadecimal de %d é %04x' % (15, 15))

'''
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')

print(f'{variavel:<10}a')
print(f'{variavel:>10}')
print(f'{variavel:^10}')
print(f'a {variavel:#^20} a')
print(f'{10000.0302032:.1f}')
print(f'{10000.0302032:,.1f}')
print(f'{-10000.0302032:+,.1f}')

print(f'o hexadecimal de 1500 é {1500:08x}')
print(f'o hexadecimal de 1500 é {1500:08X}')

