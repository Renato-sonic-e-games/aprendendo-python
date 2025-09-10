# Quantos clientes você querer cadastrar :0
# numerocli = int(input('quantos clientes tu queres cadastrar? '))

# clientes = [["jose carlos", "vanessa", "camila"], [35, 40, 10], ["Amarelo", "verde", "vermelho"]]

# print(clientes[1][2])
# print(clientes[2][1])
# print(clientes[0][2])

# vetor = [0 for i in range(numerocli)]
# for i in range(numerocli):
#     clientes.insert(i, input("nome:"))
# print(clientes)
# clientes.pop(2)
# print(clientes)

# numerocli = int(input('quantos clientes tu queres cadastrar? '))
# vetor = [0 for i in range(numerocli)]
# for i in range(numerocli):
#     print(f"\n digite os dados da pessoa: {i}")
#     nome = input("NOme: ")
#     idade = input("idade: ")
#     sexo = input("sexo: ")

#     vetor[i]= {
#         "nome": nome,
#         "idade": idade,
#         "sexo": sexo
#     }

# print("\n lista de pessoas cadastradas: ")
# for pessoas in vetor:
#     print(pessoas)

# print(vetor[0]["nome"])

from random import randint
sair = "S"
derrota = 0
vitoria = 0
while(sair=="S"):
    computador = randint(1, 11)
    userin = int(input("tente adivinhar o número sorteado de 1 a 10:"))
    if computador == userin:
        print("tu ganhou, o computador gerou: ", computador)
        vitoria = vitoria+1
    else:
        derrota = derrota+1
        print("tu perdeu, o computador gerou:", computador)
    print("você ganhou: ", vitoria, "\n e perdeu: ", derrota)
    sair = input("quer continua jogando? digite S para sim e N para não \n")
