numero_secreto=32

def entrada_usuario():
    while True:
        tentativa = input("Digite um numero: ")
        try:
            tentativa = int(tentativa)
            return tentativa
        except:
            print("Valor informado invalido!\n")


print("*********************************")
print("Bem vindo ao jogo de advinhação!!")
print("*********************************\n")

tentativa = entrada_usuario()

print("\nVocê digitou: ", tentativa)

acerto = tentativa == numero_secreto

if acerto:
    print("Você acertou!\n")

else:

    maior = tentativa > numero_secreto

    if maior:
        print("Você errou, o número secreto é menor do que o que você digitou!\n")
    else:
        print("Você errou, o número secreto é maior do que o que você digitou!\n")


print("Fim de jogo!")