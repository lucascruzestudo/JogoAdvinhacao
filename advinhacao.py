import random as rd

def numero_usuario():
    while True:
        entrada = input("Digite um número entre 1 e 50: ")
        try:
            entrada = int(entrada)
            if 1 <= entrada <= 50:
                return entrada
            else:
                print("O número deve estar entre 1 e 50!\n")
        except ValueError:
            print("Valor informado inválido! Digite um número.\n")

def verificar_entrada(entrada, numero_secreto):
    acerto = (entrada == numero_secreto)

    if acerto:
        return True, None

    else:
        maior = (numero_secreto > entrada)

        if maior:
            auxiliar = "MAIOR"
            return False, auxiliar
        else:
            auxiliar = "MENOR"
            return False, auxiliar

print("*********************************")
print("Bem vindo ao jogo de advinhação!!")
print("*********************************\n")

tentativas = 5
numero_secreto = rd.randint(1,50)

while tentativas > 0:
    print(f"Você possui {tentativas} tentativas.")
    entrada = numero_usuario()
    acertou, auxiliar = verificar_entrada(entrada, numero_secreto)
    if acertou:
        print(f"Parabéns, você acertou! O número secreto era {numero_secreto}.\n")
        break
    else:
        print(f"Você errou, o número secreto é {auxiliar} do que o número informado.\n")
    tentativas -= 1
    if (tentativas == 0):
        print(f"Acabaram suas tentativas, o número secreto era {numero_secreto}.")

print("Fim de jogo!")