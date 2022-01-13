#Exercício Python 10:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('=-'*20)
print('        CONVERSOR DE MOEDAS        ')
print('=-'*20)
valor = float(input('Qual valor em reias você tem na carteira? R$'))
dollar = valor / 3.27
print(f'Com R${valor} você poderá comprar U${dollar:.2f}')
print()
print('|Cotação do dia U$ 3.27|')