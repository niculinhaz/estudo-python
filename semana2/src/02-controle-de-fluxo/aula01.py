""" Aula 01 - Semana 2 - Operadores"""

# Operadores Aritméticos
print('1 + 1', 1 + 1, type('1 + 1'))
print('1.2 + 1.3', 1.2 + 1.3, type('1.2 + 1.3'))
n1 = 10.2
n2 = 3.5
resultado = n1 + n2 +  8.5
print('resultado', resultado, type(resultado))
print(3 - 1)
print(3 * 2, type(3*2))
print(3 / 2, type(3/2))
print(3 % 2) # resto da divisão
print(10 // 3) # mostra o resto e o quociente
print(10 ** 2) # potenciação

# Operador de Atribuição
x = 10.0
print(x)


# Operador de Comparação
resultado = x > 10
print(resultado, type(resultado))
print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))
print('10 < 10', 10 < 10, type(10 < 10))

""""condicao = x> 10.0 and resultado < 3.0
if condicao:
    pass
"""

#Operadores Lógicos
print('True and True', True and True, type(True and True))
print('True and False', True and False, type(True and False))
print('False and False', False and False, type(False and False))
print('False and True', False and True, type(False and True))

print('True or True', True or True, type(True or True))
print('True or False', True or False, type(True or False))
print('False or False', False or False, type(False or False))
print('False or True', False or True, type(False or True))

condicao = False
print('not condicao', not condicao, type(not condicao))

# Operadores Especiais

# is
# verifica se as variaveis apontam para o mesmo objeto em memoria

a = 10.0
b = 10.0
c = b
print(a==b, a==c, b==c)
print(a is b, b is c, a is c)

# in
# str, list, set, tuple, dic

frase = 'Você é um palavrão!'
print('Palavrão' in frase, type('palavrão' in frase)) 

numeros = [1, 5, 2, 6]
print(1 in numeros)


pessoa = {
    'nome' : 'Maria',
    'idade' : 22,
    'email' : 'maria@email.com'
}

print('nome' in pessoa) # verifica a existencia da chave
print('idade' in pessoa)
print('email' in pessoa)
print (22 in pessoa) # não (!!!) verifica o valor
