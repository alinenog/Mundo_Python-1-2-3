# Exercício Python 040: 
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
# no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
media = (nota1 + nota2)/2
print(f"|Sua média é : {media}|\n")
# – Média abaixo de 5.0: REPROVADO
if media < 5.0 :  
  print("Aluno Reprovado!")
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
elif  7.0 > media >= 5.0:
  print("Aluno em Recuperação!")  
# – Média 7.0 ou superior: APROVADO
elif media >= 7.0:
  print("Aluno Aprovado!!!")               

