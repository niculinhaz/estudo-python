""" Aula 05 - Tipos de Dados"""

# Numéricos
# int, float
idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String
nome = 'João'
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)
# cliente comprou um produto
produto = 'pepsi'
print(f'o cliente {nome} {sobrenome} comprou o produto {produto}')

# selecionar caracteres de uma string
# com números negativos, o python percorre a string de trás pra frente
print(nome[0], nome[-1])

print(nome.lower())
# a função lower() imprime em lower case

# separadores
print(1, 3, 7, 10, 'ahahaha', sep = '  ')

# Booleano
ligado = True
print(ligado, type(ligado))

resultado = 10 == 10
print(resultado, type(resultado))


# Listas
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
# index error = print(frutas[3])
# mudando itens da lista
frutas[0] = 'banina-nanica'
# adicionando itens ao fim da lista
frutas.append('abacaxi')
print(frutas)
# função length (tamanho)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())


# Tupla
codigos = ['SP01', 'SP02', 'SP03']
print(codigos[0])

# Tuplas são imutáveis == 
# codigos[0] = 'SP04' daria erro

print(len(codigos))


# Conjuntos (Set)
resultado_do_sorteio = {10, 4, 3, 55, 9}
print(resultado_do_sorteio)

resultado_do_sorteio.add(23)
print(resultado_do_sorteio)


# Dicionários
funcionario ={
    'nome' : 'Maria da Silva',
    'codigo' : 123,
    'salario' : 7000.00 
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['salario'])
print(funcionario['nome'])

print(funcionario.keys())
# função keys() mostra as chaves do dicionário
print(funcionario.values())
# função values() mostra e permite a manipulação dos valores do dicionário
funcionario['salario'] = 9000.00
print(funcionario['salario'])
# dicionarios permitem atribuições de valores às suas chaves
