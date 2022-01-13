#Exercício Python 34:
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para #salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de #15%.

nome=str(input('Digite o nome do funcionário: '))
salario=float(input('Digite o valor do seu salário: R$ '))
if salario >= 1250: 
  aumento = ((salario * 10)/ 100) + salario
  print(f'O novo salário do funcionário(a) {nome } será de R${aumento} apos 10% de aumento. ')
else:
  aumento = ((salario * 15)/100) + salario
  print(f'O novo salário do funcionário(a) {nome} será de R${aumento} após 15% de aumento.')  