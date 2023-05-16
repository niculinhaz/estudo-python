""" exercício 2 """

notas_inseridas = input('Insira as notas do aluno aqui, separadas por vírgula: ')
notas = notas_inseridas.split(sep = ',')

contador = 0
soma = 0
while len(notas) > contador:
     soma = float(notas[contador]) + soma
     contador+=1

media = soma / len(notas)

if media < 4.0:
   print('O aluno foi reprovado!')
elif 4.0 <= media < 6.0:
   print('O aluno está de recuperação!')
else:
   print('O aluno foi aprovado!')