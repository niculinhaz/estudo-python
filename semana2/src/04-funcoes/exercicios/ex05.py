""" Exercício 5 """

individuo = {

}

def registro():
    massa = 0
    altura = 0
    individuo['massa'] = float(input("Insira sua massa em Kg: "))
    individuo['altura'] = float(input("Insira sua altura em metros: "))
    return individuo


def calcular_imc(individuo):
    imc = individuo['massa'] / individuo['altura'] ** 2
    print(imc)
    return imc


def classificacao(imc):
    if imc < 18.5:          
       print('Baixo peso')
    if 18.5 <= imc <= 24.9:     
       print('Peso normal')
    if 25.0 <= imc <= 29.9:
        print('Excesso de peso')
    if 30.0 <= imc <= 34.9:
        print('Obesidade de Classe 1')
    if 35.0 <= imc <= 39.9:
        print('Obesidade de Classe 2')
    if imc >= 40.0:
        print('Obesidade de Classe 3')
    pass

def recomendacao(imc):
    if imc < 18.5:
       print('Recomenda-se ganhar peso.')
    if 18.5 <= imc <= 24.9:
        print('Seu IMC está bom.')
    if imc >= 25.0:
        print('Recomenda-se perder peso.')
    pass


registro()
print(individuo)
imc = calcular_imc(individuo)
classificacao(imc)
recomendacao(imc)

