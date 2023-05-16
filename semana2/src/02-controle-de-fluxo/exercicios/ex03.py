""" exercício 03 """

identificador = input('Insira aqui seu código de identificação:')
validacao1 = int(identificador[2:-1])
validacao2 = identificador[0:2]
validacao3 = identificador[-1]
if validacao1 < 0000 and validacao1 > 9999:
   print('Código inválido!')
elif validacao2 != 'BR':
   print('Código inválido')
elif validacao3 != 'X':
   print('Código inválido!')
elif len(identificador) != 7:
   print('Código inválido!') 
else:
   print('Código válido!')

