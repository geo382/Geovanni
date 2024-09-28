#Crie um programa que solicite ao usuário qual a tabuada desejada.

numero = 0

tabuada = int(input("Qual tabuada? :"))

while numero <= 10:
    print(f"{tabuada} x {numero * tabuada}")
    numero +=1 