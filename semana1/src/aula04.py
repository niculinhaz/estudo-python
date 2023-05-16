""" Aula 04 - Variáveis Constantes e Literais"""

# Variável é um espaço para armazenar dados


# python possui inferência de tipo, então não é necessário declarar
# o tipo da variável

numero = 10
print(numero)
print(type(numero))
# ou
print(numero, type(numero))
# para saber o tipo da variável

#alterando o valor de uma variável
numero = 20
print(numero)

# multiplas atribuições
nome, idade, endereço = 'Maria', 20, 'Rua...'
print(nome, idade, endereço)

# preferencialmente, atribuir cada variável em uma linha
nome = 'Maria'
idade = 20
endereço = 'Rua...'

print(nome, idade, endereço)

# atribuindo o mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)
# alterar o valor de uma não altera as outras
nome2 = 'Pedro'
print(nome1, nome2, nome3)

# python usa snake_case (pep8)
id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)
# para mudar uma variável em todas suas ocorrências, selecionar o nome da mesma e apertar F2

# Constantes
# sempre em upper case como dito na aula 01, também usando snake_case
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais
idade = 27
print(idade)
print(27)

# Numéricos
# inteiro, float ou complexo
print(10)
print(10, type(10))
print(-10, type(-10))
print(10.5, type(10.5))

# String
# para strings, podem ser usados tanto ' quanto ", mas deve ser escolhido apenas um por código
# para doc strings, sempre usar ""
# caso haja " dentro da string, usar ' para citá-la e vice versa
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's House")
print('o filme estava "excelente"')

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

# Lista
# mutável
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple)
# imutável
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails))

# Conjuntos (set)
# não permite elementos duplicados e não garante a ordem
nomes = {'maria', 'joão', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionários (dictionaries)
aluno = {
    'prontuario' : 123456,
    'nome' : 'Maria da Silva',
    'idade' : 34
        }
print(aluno, type(aluno))
