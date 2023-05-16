""" Exercício 6 """

dados_aquario = {

}
volume = 0
potencia_termo = 0
filtragem = 0

def registro():
    comprimento = 0
    altura = 0
    largura = 0
    dados_aquario['comprimento'] = float(input("Insira o comprimento do aquário em metros: "))
    dados_aquario['altura'] = float(input("Insira a altura do aquário em metros: "))
    dados_aquario['largura'] = float(input("Insira a largura do aquário em metros: "))
    return dados_aquario

def calcular_vol(dados_aquario):
    volume = dados_aquario['comprimento'] * dados_aquario['altura'] * dados_aquario['largura']
    return volume


def calcular_pot(volume):
    temperatura_desejada = int(input('Insira a temperatura desejada no aquário: '))
    temperatura_ambiente = int(input('Insira aqui a temperatura do ambiente: '))
    potencia_termo = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia_termo

def quant_filtragem(volume):
    filtragem = volume * 2
    return filtragem


registro()
volume = calcular_vol(dados_aquario)
potencia_termo = calcular_pot(volume)
filtragem = quant_filtragem(volume)
print(f'O volume do aquário, em Litros,  é {volume}')
print(f'A filtragem deve ser de 2 a 3 vezes o volume do aquário por hora, ou seja, deve ser no mínimo de {filtragem}L/h a {filtragem + volume}L/h')
print(f'Para que se mantenha a temperatura desejada na água do aquário, a potência do termostato deve ser {potencia_termo}kWh')

