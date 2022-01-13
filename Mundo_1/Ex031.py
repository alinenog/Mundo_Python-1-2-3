#Exercício Python 31:
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, #cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

''' If simplificado

km=float(input('Digite quantos km são sua viagem: '))
valor = km * 0.50 if km <= 200 else km * 0.45
print(f'A passagem de {km}km. será de R${valor}')
'''

km = float(input('Digite quantos km são sua viagem: '))
if km <= 200:
  valor = km * 0.50
  print(f'O valor da sua passagem será de R${valor}')
else:
  valor = km * 0.45
  print(f'O valor da sua passagem será R${valor}')  