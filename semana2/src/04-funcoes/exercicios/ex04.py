""" Exercicio 04 """

def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = numero + resultado
    return resultado