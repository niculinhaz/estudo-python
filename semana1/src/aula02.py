"""  aula 02 - keywords e identificadores"""

# palavras reservadas
# True, False (booleanos), None, and, lambda

# identificadores
# nome de variáveis, classes, funções, estruturas
# python é case sensitive, então nome =/ Nome =/ NOME
# devem iniciar com letra ou _, geralmente com letra
# não pode ter espaços em branco

nome = 'Maria'
# identificador = nome
idade = 30
# identificador = idade
nome_completo = 'Maria da Silva'
# identificador = nome_completo (não podem haver espaços e nem caracteres especiais, como @ ou !;)
# para separar palavras é usado o _

# Clean Code
c = 10
contador = 10
# sempre deixar claro o uso da variável, para claro entendimento do código

nome.upper()
# upper() retorna todos caracteres do identificador em letras maiusculas

# Constantes
# sempre definir constantes em letras maiúsculo
PI = 3.14

idade = 18
#definir uma constante para maioridade, para ajudar no entendimento
MAIORIDADE = 18

if idade >= MAIORIDADE:
    print('Maior de idade')
else:
    print('Menor de idade')