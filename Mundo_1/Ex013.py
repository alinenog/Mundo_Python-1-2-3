# Exercício Python 13:
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = str(input('Digite o nome do funcionário?'))
sal = float(input('Digite o valor do salário atual R$'))
aumento = sal + ((sal*15)/100)
print('| O novo salário do fúncionario(a) {} será R${:.2f} após aumento de 15% |'.format(nome,aumento))
