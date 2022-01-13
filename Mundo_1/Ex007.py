# Exercício Python 7:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Digite seu nome: ')
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno: '))
media= n1 + n2 /2
print('A média esolar de {} é {}!'.format(nome,media))
