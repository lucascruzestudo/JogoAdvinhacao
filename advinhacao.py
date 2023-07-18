import random as rd
from time import sleep

def definir_dificuldade():
    dificuldades = [["Fácil",10],["Difícil",5],["Insano",3]]
    while True:
        print("Selecione uma dificuldade")
        print("(0) Fácil, 10 tentativas\n(1) Difícil, 5 tentativas\n(2) Insano, 3 tentativas\n")
        escolhida = input("Dificuldade escolhida entre 0 e 2: ")
        try:
            escolhida = int(escolhida)
            if 0 <= escolhida <= 2:
                print(f"\nDificuldade {dificuldades[escolhida][0]} selecionada!")
                print("Iniciando partida...\n")
                sleep(2)
                return dificuldades[escolhida][1]
            else:
                print("As dificuldades vão de 0 a 2!\n")
        except ValueError:
            print("Valor informado inválido! Digite um número entre 0 e 2!\n")

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

tentativas = definir_dificuldade()
numero_secreto = rd.randint(1,50)
pontos = 1000

while tentativas > 0:
    print(f"Você possui {tentativas} tentativas.")
    entrada = numero_usuario()
    acertou, auxiliar = verificar_entrada(entrada, numero_secreto)
    if acertou:
        print(f"Parabéns, você acertou! O número secreto era {numero_secreto}.\n")
        break
    else:
        print(f"Você errou, o número secreto é {auxiliar} do que o número informado.\n")
        pontos_perdidos = abs(numero_secreto - entrada)
        pontos -= pontos_perdidos
    tentativas -= 1
    if (tentativas == 0):
        print(f"Acabaram suas tentativas, o número secreto era {numero_secreto}.")
        pontos = 0

print("Fim de jogo!")
print(f"Sua pontuação: {pontos}")