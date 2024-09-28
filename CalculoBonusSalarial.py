#Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
#for superior a 5 anos, conceda um bônus de 5% ao salário. Ao final deve ser mostrado o salário atualizado.
salario = float(input("Inserir seu salário:"))
tempodeservico = float(input("Inserir seu tempo de serviço:"))

if tempodeservico >= 5:
    print(f"Seu salario é {salario+salario*0.05}")
else :
    print(f"{salario}")