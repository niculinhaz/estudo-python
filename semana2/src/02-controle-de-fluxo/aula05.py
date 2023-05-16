""" Aula 05 - Break e Continue """

for i in range(10):
    if i == 4:
        break
    print(i)

# encontrar a posicao de um numero
# de uma lista de inteiros. Caso nao
# encontre posicao e igual a -1

busca = 5
numeros = [1, 5, 9, 7, 1, 3, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break
    contador += 1

print(posicao)

# for i in range(len(numeros)):
#     print('Procurando na posicao:', i)
#     if numeros[i] == busca:
#         posicao = i
#         break

# print(posicao)

# continue 
# pula a iteração atual
print('-----')
for numero in numeros:
    if numero == 3:
        continue
    print(numero)