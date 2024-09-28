#Atividade 1 
#Existe um calculo que faz a correção do peso e altura de um individuo, o IMC (índice de massa corporal). 
# Para calcular o IMC de uma pessoa devemos saber sua altura, seu peso e aplicar a formula "IMC = Peso / altura²;
#Crie um programa que solicite o nome, peso e altura de uma pessoa. Ao final saúde a pessoa e mostre o resultado 
# do IMC.

nome = input("Digite seu nome:") 
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
altura = altura * altura
imc = peso / altura



print (f" Seu IMC é: {imc:.2f}")
