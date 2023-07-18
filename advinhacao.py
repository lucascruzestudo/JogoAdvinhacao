import random as rd

def numero_usuario():
    while True:
        entrada = input("Digite um numero: ")
        try:
            entrada = int(entrada)
            return entrada
        except:
            print("Valor informado invalido!\n")

def verificar_entrada(entrada, numero_secreto):
    acerto = (entrada == numero_secreto)

    if acerto:

        return True, None

    else:

        maior = (numero_secreto > entrada)

        if maior:
            return False, "MAIOR"
        else:
            return False, "MENOR"



print("*********************************")
print("Bem vindo ao jogo de advinhação!!")
print("*********************************\n")

tentativas = 10
numero_secreto = rd.randint(1,100)

while tentativas > 0:
    print(f"Você possui {tentativas} tentativas.")
    entrada = numero_usuario()
    acertou, auxiliar = verificar_entrada(entrada, numero_secreto)
    if acertou:
        print("Parabéns, você acertou!\n")
        break
    else:
        print(f"Você errou, o número secreto é {auxiliar} do que o número informado.\n")
    tentativas -= 1

print("Fim de jogo!")