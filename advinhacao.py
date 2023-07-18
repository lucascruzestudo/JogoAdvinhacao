import random as rd

numero_secreto= rd.randint(1,100)

def numero_usuario():
    while True:
        entrada = input("Digite um numero: ")
        try:
            entrada = int(entrada)
            return entrada
        except:
            print("Valor informado invalido!\n")

def verificar_entrada(entrada, numero_secreto):
    print("\nVocê digitou: ", entrada)
    acerto = (entrada == numero_secreto)

    if acerto:

        print("Você acertou!\n")
        return True

    else:

        maior = (entrada > numero_secreto)

        if maior:
            print("Você errou, o número secreto é menor do que o que você digitou!\n")
        else:
            print("Você errou, o número secreto é maior do que o que você digitou!\n")

        return False


print("*********************************")
print("Bem vindo ao jogo de advinhação!!")
print("*********************************\n")



while True:
    entrada = numero_usuario()
    encerramento = verificar_entrada(entrada, numero_secreto)
    if encerramento == True:
        print("Fim de jogo!")
        break