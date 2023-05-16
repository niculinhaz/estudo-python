""" Aula 07 - Entrada e Saída"""

# saída padrão ou SSI ( Sytem Standart Output)
print('hello World', 'Maria', 1, True, end = '!!!\n')
# considera os valores numa tupla
# sep= '' define o separador, que é colocado entre os valores#
# end ='' define o final do output, como por exemplo, \n para criar uma nova linha
print('hello World', 'Maria', 1, True, sep = '@', end= '')

#escrita em arquivo
arquivo = open('nomes.txt', 'w', encoding= 'utf-8')
print('joao@email.com', 'maria@email.com', 'pedro@email.com', file = arquivo, sep= ';', end='\n')


# Entrada de dados
nome = input("digite seu nome:")
idade = input("digite sua idade:")
idade = int(idade)
#ou substitua as duas últimas linhas por idade = int(input("digite sua idade:"))
print(nome.upper())
print(idade, type(idade))

if idade>= 18:
    print(f'{nome}, você é maior de idade.')
else:
    print(f'{nome}, você é menor de idade.')

# leitura de arquivos
arquivo_notas = open('notas.txt', 'r', encoding= 'utf-8')
conteudo = arquivo_notas.read()
# print(conteudo) para ler todo texto do arquivo
# para leitura individual do conteúdo do arquivo:
notas = conteudo.split(sep=';')
# para conversão do conteúdo do arquivo de string para valor numérico
notas = [float(notas) for nota in notas]
print (notas)
# calcular a partir dos valores lidos no arquivo
media = (notas[0] + notas[1] + notas[2])/len(notas)
print(media)
