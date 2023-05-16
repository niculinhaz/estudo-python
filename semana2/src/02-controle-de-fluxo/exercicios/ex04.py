""" Exercício 04 """

ERROS = ["O identificador não começa com BR", "O identificador não possui numeração entre 0000 e 9999", "O identificador não termina com 'X'", "O identificador não tem 7 dígitos"]
identificador = input('Insira aqui seu código de identificação:')
validacao1 = int(identificador[2:-1])
validacao2 = identificador[0:2]
validacao3 = identificador[-1]
if validacao1 < 0000 or validacao1 > 9999:
   print(ERROS[1])
if validacao2 != 'BR':
   print(ERROS[0])
if validacao3 != 'X':
   print(ERROS[2])
if len(identificador) != 7:
   print(ERROS[3])
if validacao1 < 0000 or validacao1 > 9999 or validacao2 != 'BR' or validacao3 != 'X' or len(identificador) != 7:
    print('Código inválido!')
else:
   print('Código válido!')
