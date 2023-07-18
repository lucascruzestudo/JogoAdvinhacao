numero_secreto=32

print("*********************************")
print("Bem vindo ao jogo de advinhação!!")
print("*********************************\n")

while True:
    tentativa = input("Digite um numero: ")
    try:
        tentativa = int(tentativa)
        break
    except:
        print("Valor informado invalido!\n")

print("Você digitou", tentativa)

if numero_secreto == tentativa:
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de jogo!")