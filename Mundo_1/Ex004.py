# Exercício Python 4:
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações #possíveis  sobre ele..'''

e=input('Digite algo:') 
print('Entrada é um número: ',e.isnumeric())
print('Entrada é decimal:',e.isdecimal())
print('Entrada é alfabetica:',e.isalpha())
print('Esta em maisculas ?', e.isupper())
print('Esta em minusculas ?',e.islower())
print('Esta capitalizada',(e.istitle()))
print('É alfabético ?',e.isalpha())
print('E alfanumerico ? ',e.isalnum())
print('Só tem espaços ? ',e.isspace())
