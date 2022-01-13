#Exercício Python 15:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de #dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 #por Km rodado.

print('------------------------------')
print('    LOCADORA DE VEÍCULOS      ')
print('------------------------------')
print('| Dia de aluguel R$ 60.00    |')
print('| R$ 0.15 por Km rodado      |')
print('------------------------------')
print()
dias = int(input('Quantos dias de aluguel?'))
km = float(input('Quantos kilomêtros foram percorridos? '))
#Calculo
t_dias= dias * 60
t_km = km * 0.15
print()
print('Valor total a pagar R$ {:5.2f}'.format(t_dias + t_km))
print()
print('------ Relatório de despesas ------')
print(f'RS {t_dias:5.2f} referente aos dias de aluguel do veículo')
print(f'R$ {t_km} referente a {km} km rodados')