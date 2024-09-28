#Crie um programa que simule um sistema básico de reserva de voos. O programa deve permitir que o usuário
#adicione reservas de voos enquanto desejar. Cada reserva deve incluir o nome do passageiro e o destino. Ao final, o
#programa deve listar todas as reservas feitas.

nomes = []
destinos = []

continua = "s"
while continua == "s":
    nome = input("Digite um nome: ")
    nomes.append(nome)
    destino = input("Digite o destino: ")
    destinos.append(destino)
    continua = input("Deseja continuar?: ")
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}, Destino: {destinos[i]} ")
