""" Aula 02 - Instrução if """

# if condicao:
#     instrucao
#     instrucao
#     instrucao


# C, Java, C#, outras
# if() {
#     instrucao
#  instrucao
# }

codigo_cliente = 32
valor_desconto = 23.0
desconto_especial = valor_desconto >= 20.0

if desconto_especial:
    print('Desconto Especial')
    print(codigo_cliente)
else:
    print("Sem desconto especial")


# Nome tem que ter pelo menos tres caracteres
nome = 'Loe'

print(len(nome), type(len(nome)))

nome_invalido = len(nome) < 3

if nome_invalido:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

nome_valido = len(nome) >= 3
if nome_valido:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')


if not nome_invalido:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')


# Nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Loe'
idade = 18
erros = []


nome_invalido = len(nome) < 3
if nome_invalido:
    erros.append('Nome deve ter pelo menos 3 caracteres')

idade_invalida = idade < 18
if idade_invalida:
    erros.append('Idade deve ser maior ou igual a 18')

# False: False, None, 0,0.0, string vazia '', lista, tuple, set vazio
# True: todo o resto
if erros:
    print(erros)
else:
    print('Dados válidos')


# if elif else

# Verifica se um número é positivo ou negativo ou zero
numero = 3

# ______________ _ _________
# -N -4 -3 -2 -1 0 1 2 3 4 N
if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')


# calcule a média e verifique se as duas notas
# são válidas antes do cálculo
n1 = 5.6
n2 = 10.0

# Cuidado com o if aninhado
if n1 >= 0 and n1 <= 10:
    if n2 >= 0 and n2 <= 10:
        # media =
        pass
    else:
        print('Notas Inválidas')
else:
    print('Notas inválidas')


nota1_valida = 0 <= n1 <= 10
nota2_valida = 0 <= n2 <= 10

if nota1_valida and nota2_valida:
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas Inválidas')