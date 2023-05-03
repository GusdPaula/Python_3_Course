# copy, sorted, produtos.sort

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Exercícios

# Aumente os preços dos produtos a seguir em 10%

for produto in produtos:
    produto['preco'] *= 1.10
    produto['preco'] = round(produto['preco'], 2)


#print(produtos)

# Gere novos_produtos por deep copy (cópia profunda)

produto_6 = copy.deepcopy(produtos[0])
produto_6['nome'] = 'Produto 6'
produto_6['preco'] = 100.00

produtos.append(produto_6)

#print(produtos)


# Ordene os produtos por nome decrescente (do maior para menor)
produtos = sorted(produtos, key=lambda x: x['nome'], reverse=True)

#print(produtos)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
new_produtos = copy.deepcopy(produtos)

#print(new_produtos)

# Ordene os produtos por preco crescente (do menor para maior)
produtos = sorted(produtos, key=lambda x: x['preco'])

#print(produtos)

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
new_produtos = copy.deepcopy(produtos)

print(new_produtos)