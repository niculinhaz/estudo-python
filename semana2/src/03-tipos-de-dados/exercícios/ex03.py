""" Exercício 03 """

numero = int(input('Insira o número do mês:'))

mes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

if numero < 1 or numero > 12:
   print('Número Inválido!')
else:
   print(f"O mês selecionado foi {mes[numero]}")