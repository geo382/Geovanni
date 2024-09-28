#Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
#"A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).
nota = float(input("Digite uma nota 0 a 100:"))

if nota > 100 :
    print("é maior que 100! não pode!")
elif nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 60:
    print("Nota C")
elif nota <=60:
    print("Nota F")