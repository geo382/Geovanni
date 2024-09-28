#Crie um programa que peça ao usuário para inserir sua idade e, em
#seguida, informe se a pessoa é menor de idade ou maior de idade.

idade = int(input("Insera sua idade:"))

if idade < 18:
    print("Menor de idade")
elif idade > 18:
    print("Maior de idade")
    