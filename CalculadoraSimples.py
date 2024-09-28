#Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#Realize a operação e exiba o resultado.]

print("insira dois números e uma operação.")
numero1 = float(input("insira um número:"))
numero2 = float(input("insira um número:"))
operacao = input("insira o operador +, -, / ou *")

if operacao == "+":
    print(f"resultado: {numero1+numero2}")
elif operacao == "-":
    print(f"resultado: {numero1-numero2}")
elif operacao == "/":
    if numero2 == 0:
        print("nao e possivel dividir por 0!")
    else:
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    print(f"resultado: {numero1/numero2}")
elif operacao == "*":
    print(f"resultado: {numero1*numero2}")