""" Aula 06 - Coversão de tipos"""

# Conversão de tipo implícita
leitura = 5.53
peso = 3
total = leitura * peso
# python converte peso em float para realizar o cálculo
print(total, type(total))

# Conversão de tipo explícita (Type casting)
# soma = 13.4 + '3.5'
# para converter a string '3.5' em valor numérico, usa-se a função float()
soma = 13.4 + float('13.5')
print(soma, type(soma))

idade = '32'
# para converter a string '32' em valor numérico, usa-se a função int()
idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70
# para converter o valor numérico "170" para string, usa-se a função str()

mensagem = nome + 'tem a altura de' + str(altura)
print(mensagem)
#não precisa de conversão 
mensagem = f'{nome} tem a altura de {altura}'
print(mensagem)
