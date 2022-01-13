# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Ex:Digite uma distância em metros: 185.72 A distância de 85.7m corresponde a:
# 0.18572Km | 1.8572Hm | 18.572Dam | 1857.2dm | 18572.0cm | 185720.0mm

print('='*26)
print('   CALCÚLO DE DISTÂNCIA   ')
print('='*26)
m = float(input('Digite uma distância em metros: '))

#Calculo de Milímetros
mm = m * 1000
#Calculo de Centímetros
cm = m * 100
#Calculo de Decímetros
dm = m * 10
#Calculo de Kilômetros
km = m / 1000
#Calculo de Hectômetro
hm = m / 100
#Calculo de Decâmetro
dam = m / 10

print('A distância de {} metros é referente a {:.0f} Milímetros'.format(m,mm ))
print('A distância de {} metros é referente a {:.0f} Centímetros'.format(m,cm ))
print('A distância de {} metros é referente a {:.0f} Decímetros'.format(m, dm))
print('A distância de {} metros é referente a {} Kilômetros'.format(m,km ))
print('A distância de {} metros é referente a {} Hectômetro'.format(m,hm ))
print('A distância de {} metros é referente a {} Decâmetro'.format(m,dam ))
