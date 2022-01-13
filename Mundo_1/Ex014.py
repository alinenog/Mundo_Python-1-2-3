#Exercício Python 14:
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('__________________________________')
print('    CONVERSOR DE TEMPERATURA      ')
print('__________________________________')
print('''
     [1] Celsius para Fahrenheit
     [2] Celsius para Kelvin
     [3] Fahrenheit para Celsius
     [4] Fahrenheit para Kelvin
     [5] Kelvin para Celsius
     [6] Kelvin para Fahrenheit 
''')
opcao = int(input('Digite sua opção:'))
temp = float(input('Digite o valor a ser convertido:'))
print()

# Celsius para Fahrenheit
if opcao == 1:
    fah = ((temp * 9) / 5) + 32
    print(f'A temperatura de {temp} Celsius corresponde a {fah} Fahrenheit')

# Celsius para Kelvin
elif opcao == 2:
    kel = (temp + 273.15)
    print(f'A temperatura de {temp} Celsius corresponde a {kel} Kelvin')

# Fahrenheit para Celsius
elif opcao == 3:
    cel = (((temp - 32) * 5) / 9)
    print(f'A temperatura de {temp} Fahrenheit corresponde a {cel:.2f} Celsius')

# Fahrenheit para Kelvin
elif opcao == 4:
    kel = (((temp - 32) * 5 )/9+273.15)
    print(f'A temperatura de {temp} Fahrenheit corresponde a {kel:.2f} Kelvin')

# Kelvin para Celsius
elif opcao == 5:
    cel = (temp - 273.15)
    print(f'A temperatura de {temp} Kelvin corresponde a {cel:.2f} Celsius ')

# Kelvin para Fahrenheit
elif opcao == 6:
    fah = ((temp - 273.15 ) * 9)/5 + 32
    print(f'A temperatura de {temp} Kelvin corresponde a {fah:.2f} Fahrenheit ')
 
