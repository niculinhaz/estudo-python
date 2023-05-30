""" Aula 01 - Introdução a Orientação a objetos """

# paradigma de programação

# calcular a área e o perímetro de um retângulo
# área = base * altura
# perímetro = 2*(base + altura)
# estrutura para armazenar os valores necessários para os cálculos

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

# Realizar os calculos


def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']


def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])


print(calcular_area(retangulo1))
print(calcular_area(retangulo2))
print(calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo2))


# Classe representa um conceito
# Essa classe representa um retangulo
# Classe possui atributos base e altura
# Classe possui metodos (funcao dentro da classe)
# Self é apenas um nome por padrão
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# Instanciando objetos do tipo Retangulo
# Chamando o metodo construtor
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)

print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(
    retangulo1.base,
    retangulo1.altura,
    retangulo1.calcular_area(),
    retangulo1.calcular_perimetro()
)
print(
    retangulo2.base,
    retangulo2.altura,
    retangulo2.calcular_area(),
    retangulo2.calcular_perimetro()
)
