""" Exercício 01 """

numeros = []

for numero in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

menor = numero[0]
maior = numero[0]
for numero in numeros:
    if maior > numero:
        numero = maior
    if menor < numero:
        numero = menor

print(f'o menor e o maior número são: {maior} e {menor}')

        